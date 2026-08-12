# -*- coding: utf-8 -*-
"""
prediction_cn_markets_day.py

Description:
    Two-phase prediction for A-share daily K-line data using Kronos model and xtquant (QMT).

    Phase 1 — Backtest:
        Train on 2020-01-01 ~ 2025-12-31 data, predict from 2026-01-01 to today
        (actual number of trading days YTD).
        Overlay predicted close vs actual close to visually assess accuracy.

    Phase 2 — Forward:
        Train on 2020-01-01 ~ today data, predict next 120 trading days.

    Both predictions are overlaid on a single chart.

Usage:
    python prediction_cn_markets_day.py --symbol 000001.SZ

Arguments:
    --symbol     Stock code with exchange suffix (e.g. 000001.SZ, 600519.SH, 002594.SZ)

Output:
    - ./outputs/pred_<symbol>_chart.png  — combined chart
    - ./outputs/pred_<symbol>_data.csv   — full merged CSV
"""

import os
import argparse
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

sys.path.append("../")
from model import Kronos, KronosTokenizer, KronosPredictor
from data_driver.mini_qmt import get_data_from_xtdata

save_dir = "./outputs"
os.makedirs(save_dir, exist_ok=True)

# Setting
TOKENIZER_PRETRAINED = "NeoQuasar/Kronos-Tokenizer-base"
MODEL_PRETRAINED = "NeoQuasar/Kronos-base"
DEVICE = "cpu"  # "cuda:0"
MAX_CONTEXT = 512
LOOKBACK = 400
PRED_LEN = 120
T = 1.0
TOP_P = 0.9
SAMPLE_COUNT = 1


def load_data(symbol: str, start_date: datetime, end_date: datetime) -> pd.DataFrame:
    print(f"📥 Fetching {symbol} daily data from xtquant ({start_date.date()} ~ {end_date.date()}) ...")

    dfs = get_data_from_xtdata(
        symbols=[symbol],
        startdate=start_date,
        enddate=end_date,
        interval="1d",
    )

    if symbol not in dfs or dfs[symbol] is None or dfs[symbol].empty:
        print(f"❌ Failed to fetch data for {symbol}. Exiting.")
        sys.exit(1)

    df = dfs[symbol].copy()

    df = df.reset_index()
    df.rename(columns={
        "datetime": "date",
    }, inplace=True)

    df["date"] = pd.to_datetime(df["date"]).dt.tz_localize(None)
    df = df.sort_values("date").reset_index(drop=True)

    df["amount"] = df["close"] * df["volume"]

    numeric_cols = ["open", "high", "low", "close", "volume", "amount"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Fix invalid open values
    open_bad = (df["open"] == 0) | (df["open"].isna())
    if open_bad.any():
        print(f"⚠️  Fixed {open_bad.sum()} invalid open values.")
        df.loc[open_bad, "open"] = df["close"].shift(1)
        df["open"].fillna(df["close"], inplace=True)

    before = len(df)
    df = df.dropna(subset=numeric_cols).reset_index(drop=True)
    if len(df) < before:
        print(f"⚠️  Dropped {before - len(df)} rows with NaN values.")

    print(f"✅ Data loaded: {len(df)} rows, range: {df['date'].min()} ~ {df['date'].max()}")
    return df


def prepare_inputs(df, lookback, pred_len):
    x_df = df.iloc[-lookback:][["open", "high", "low", "close", "volume", "amount"]]
    x_timestamp = df.iloc[-lookback:]["date"]
    y_timestamp = pd.bdate_range(
        start=df["date"].iloc[-1] + pd.Timedelta(days=1),
        periods=pred_len,
    )
    return x_df, pd.Series(x_timestamp), pd.Series(y_timestamp)


def apply_price_limits(pred_df, last_close, limit_rate=0.1):
    print(f"🔒 Applying ±{limit_rate * 100:.0f}% price limit ...")

    pred_df = pred_df.reset_index(drop=True)
    cols = ["open", "high", "low", "close"]
    pred_df[cols] = pred_df[cols].astype("float64")

    for i in range(len(pred_df)):
        limit_up = last_close * (1 + limit_rate)
        limit_down = last_close * (1 - limit_rate)

        for col in cols:
            value = pred_df.at[i, col]
            if pd.notna(value):
                clipped = max(min(value, limit_up), limit_down)
                pred_df.at[i, col] = float(clipped)

        last_close = float(pred_df.at[i, "close"])

    return pred_df


def run_prediction(predictor, df, lookback, pred_len, last_close):
    """Run a single prediction and return the pred_df with date column."""
    if len(df) < lookback:
        print(f"⚠️  Insufficient data: need {lookback} rows, got {len(df)}. Skipping.")
        return None

    x_df, x_timestamp, y_timestamp = prepare_inputs(df, lookback, pred_len)

    print("🔮 Generating predictions ...")
    pred_df = predictor.predict(
        df=x_df,
        x_timestamp=x_timestamp,
        y_timestamp=y_timestamp,
        pred_len=pred_len,
        T=T,
        top_p=TOP_P,
        sample_count=SAMPLE_COUNT,
    )

    pred_df["date"] = y_timestamp.values
    pred_df = apply_price_limits(pred_df, last_close, limit_rate=0.1)
    return pred_df


def plot_combined(df_all, pred_backtest, pred_forward, symbol, split_date):
    """Plot all three series on one chart."""
    fig, ax = plt.subplots(figsize=(14, 7))

    # Full historical close
    ax.plot(df_all["date"], df_all["close"], label="Historical Close", color="blue", linewidth=1.2)

    # Phase 1: backtest prediction (2026 YTD)
    if pred_backtest is not None:
        ax.plot(pred_backtest["date"], pred_backtest["close"],
                label="Backtest Pred (2026 YTD)", color="orange", linestyle="--", linewidth=1.5)

    # Phase 2: forward prediction (next 120 days)
    if pred_forward is not None:
        ax.plot(pred_forward["date"], pred_forward["close"],
                label="Forward Pred (next 120d)", color="red", linestyle="--", linewidth=1.5)

    # Vertical line at the split (start of 2026)
    ax.axvline(x=split_date, color="gray", linestyle=":", alpha=0.6, label=f"Train/Test split ({split_date.date()})")

    ax.set_title(f"Kronos Prediction for {symbol}", fontsize=14)
    ax.set_xlabel("Date")
    ax.set_ylabel("Close Price")
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    fig.autofmt_xdate()
    plt.tight_layout()

    safe_symbol = symbol.replace(".", "_")
    plot_path = os.path.join(save_dir, f"pred_{safe_symbol}_chart.png")
    plt.savefig(plot_path, dpi=150)
    plt.close()
    print(f"📊 Chart saved: {plot_path}")


def predict_future(symbol):
    print(f"🚀 Loading Kronos tokenizer: {TOKENIZER_PRETRAINED} model: {MODEL_PRETRAINED} ...")
    tokenizer = KronosTokenizer.from_pretrained(TOKENIZER_PRETRAINED)
    model = Kronos.from_pretrained(MODEL_PRETRAINED)
    predictor = KronosPredictor(model, tokenizer, device=DEVICE, max_context=MAX_CONTEXT)

    today = datetime.today()

    # ── Phase 1: Backtest ──────────────────────────────────────────
    # Train: 2020-01-01 ~ 2025-12-31
    # Predict: 2026-01-01 ~ today (actual number of trading days YTD)
    print("\n" + "=" * 60)
    print("📌 Phase 1: Backtest — predict 2026 YTD using data up to 2025-12-31")
    print("=" * 60)

    train_end_2025 = datetime(2025, 12, 31)
    df_phase1 = load_data(symbol, datetime(2020, 1, 1), train_end_2025)

    # Count actual trading days from 2026-01-01 to today
    year_start = datetime(2026, 1, 1)
    backtest_pred_len = len(pd.bdate_range(start=year_start, end=today))
    print(f"📐 2026 YTD trading days: {backtest_pred_len}")

    if len(df_phase1) >= LOOKBACK and backtest_pred_len > 0:
        # Ensure total context (lookback + pred_len) does not exceed MAX_CONTEXT
        phase1_lookback = min(LOOKBACK, MAX_CONTEXT - backtest_pred_len)
        if phase1_lookback < 100:
            print(f"⚠️  Backtest pred_len ({backtest_pred_len}) leaves only {phase1_lookback} lookback, too small. Skipping.")
            pred_backtest = None
        else:
            if phase1_lookback < LOOKBACK:
                print(f"⚠️  Reducing lookback to {phase1_lookback} to stay within MAX_CONTEXT={MAX_CONTEXT}")
            last_close_phase1 = df_phase1["close"].iloc[-1]
            pred_backtest = run_prediction(predictor, df_phase1, phase1_lookback, backtest_pred_len, last_close_phase1)
    else:
        print(f"⚠️  Phase 1: only {len(df_phase1)} rows or 0 pred_len. Skipping backtest.")
        pred_backtest = None

    # ── Phase 2: Forward ───────────────────────────────────────────
    # Train: 2020-01-01 ~ today
    # Predict: next 120 trading days
    print("\n" + "=" * 60)
    print("📌 Phase 2: Forward — predict next 120 trading days using all data up to today")
    print("=" * 60)

    df_all = load_data(symbol, datetime(2020, 1, 1), today)

    if len(df_all) >= LOOKBACK:
        last_close_all = df_all["close"].iloc[-1]
        pred_forward = run_prediction(predictor, df_all, LOOKBACK, PRED_LEN, last_close_all)
    else:
        print(f"⚠️  Phase 2: only {len(df_all)} rows, need {LOOKBACK}. Skipping forward.")
        pred_forward = None

    # ── Plot ───────────────────────────────────────────────────────
    split_date = pd.Timestamp("2026-01-01")
    plot_combined(df_all, pred_backtest, pred_forward, symbol, split_date)

    # ── Save CSV ───────────────────────────────────────────────────
    rows = [df_all[["date", "open", "high", "low", "close", "volume", "amount"]]]
    labels = []
    if pred_backtest is not None:
        rows.append(pred_backtest[["date", "open", "high", "low", "close", "volume", "amount"]])
        labels.append("backtest")
    if pred_forward is not None:
        rows.append(pred_forward[["date", "open", "high", "low", "close", "volume", "amount"]])
        labels.append("forward")

    df_out = pd.concat(rows).reset_index(drop=True)
    safe_symbol = symbol.replace(".", "_")
    out_file = os.path.join(save_dir, f"pred_{safe_symbol}_data.csv")
    df_out.to_csv(out_file, index=False)
    print(f"✅ Data saved: {out_file}")

    # ── Print summary ──────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📊 Summary")
    print("=" * 60)
    print(f"  Symbol:          {symbol}")
    print(f"  Historical rows: {len(df_all)}")
    print(f"  Backtest pred:   {'✅' if pred_backtest is not None else '❌'}  ({len(pred_backtest) if pred_backtest is not None else 0} days)")
    print(f"  Forward pred:    {'✅' if pred_forward is not None else '❌'}  ({len(pred_forward) if pred_forward is not None else 0} days)")
    print(f"  Chart:           {os.path.join(save_dir, f'pred_{safe_symbol}_chart.png')}")
    print(f"  CSV:             {out_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Kronos stock prediction script (xtquant data source)")
    parser.add_argument("--symbol", type=str, default="000001.SZ", help="Stock code with exchange suffix (e.g. 000001.SZ, 600519.SH)")
    args = parser.parse_args()

    predict_future(symbol=args.symbol)
