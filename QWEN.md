# Kronos — QWEN.md

## Project Overview

**Kronos** is the first open-source foundation model for financial candlestick (K-line) data, accepted by **AAAI 2026**. It is a family of decoder-only Transformer models pre-trained on data from 45+ global exchanges.

### Architecture (Two-Stage)

1. **Tokenizer** (`KronosTokenizer`): A hybrid quantizer (Binary Spherical Quantization) that compresses continuous multi-dimensional OHLCV data into hierarchical discrete tokens (s1-bits / s2-bits). Uses encoder-decoder Transformer blocks.
2. **Predictor** (`Kronos`): An autoregressive Transformer that operates on the discrete token sequence produced by the tokenizer, enabling unified forecasting across diverse quantitative tasks.

### Model Variants

| Model | Tokenizer | Context | Params | Open-source |
|-------|-----------|---------|--------|-------------|
| Kronos-mini | Tokenizer-2k | 2048 | 4.1M | ✅ |
| Kronos-small | Tokenizer-base | 512 | 24.7M | ✅ |
| Kronos-base | Tokenizer-base | 512 | 102.3M | ✅ |
| Kronos-large | Tokenizer-base | 512 | 499.2M | ❌ |

### Key Dependencies

- Python ≥ 3.11
- PyTorch ≥ 2.0
- einops, huggingface-hub, safetensors, pandas, numpy, matplotlib, tqdm

---

## Directory Structure

```
D:\workspace\Kronos\
├── main.py                          # Entry point (placeholder)
├── pyproject.toml                   # Project metadata & dependencies
├── requirements.txt                 # pip dependencies
├── uv.lock                          # uv lockfile
├── QWEN.md                          # This file
│
├── model/                           # Core model implementation
│   ├── __init__.py                  # Exports KronosTokenizer, Kronos, KronosPredictor
│   ├── kronos.py                    # Tokenizer, Predictor, and main Kronos model (~663 lines)
│   └── module.py                    # Building blocks: BSQuantizer, TransformerBlock, etc. (~571 lines)
│
├── data_driver/                     # Data fetching utilities
│   ├── __init__.py
│   └── mini_qmt.py                  # xtquant-based data downloader for Chinese markets
│
├── examples/                        # Usage examples
│   ├── prediction_example.py        # Basic forecasting example
│   ├── prediction_wo_vol_example.py # Forecasting without volume/amount
│   ├── prediction_batch_example.py  # Batch prediction on multiple series
│   ├── prediction_new.py            # Extended prediction script
│   ├── prediction_new_GUI.py        # GUI-based prediction
│   ├── prediction_akshare_2024-2025.py
│   ├── prediction_cn_markets_day.py
│   ├── get_akshare_date_2024-2025_x.py
│   ├── get_date_new.py
│   ├── run_backtest_kronos.py
│   └── yuce/                        # Additional prediction scripts
│
├── finetune/                        # Qlib-based finetuning pipeline (A-share market)
│   ├── config.py                    # Centralized configuration
│   ├── dataset.py                   # QlibDataset
│   ├── qlib_data_preprocess.py      # Data preprocessing from Qlib
│   ├── qlib_test.py                 # Backtesting evaluation
│   ├── train_tokenizer.py           # Tokenizer finetuning (multi-GPU via torchrun)
│   ├── train_predictor.py           # Predictor finetuning (multi-GPU via torchrun)
│   └── utils/                       # Utility modules
│
├── finetune_csv/                    # CSV-based finetuning pipeline (any market)
│   ├── README.md                    # Detailed documentation
│   ├── config_loader.py             # YAML config loader
│   ├── train_sequential.py          # Sequential training (tokenizer → predictor)
│   ├── finetune_tokenizer.py        # Standalone tokenizer finetuning
│   ├── finetune_base_model.py       # Standalone predictor finetuning
│   ├── configs/
│   │   └── config_ali09988_candle-5min.yaml  # Example config (Alibaba HK stock)
│   ├── data/
│   │   └── HK_ali_09988_kline_5min_all.csv   # Example dataset
│   └── examples/                    # Training result visualizations
│
├── webui/                           # Flask-based web interface
│   ├── app.py                       # Flask application (~709 lines)
│   ├── run.py                       # Launcher script
│   ├── start.sh                     # Shell launcher
│   ├── requirements.txt             # Web UI dependencies
│   ├── README.md                    # Web UI documentation
│   ├── templates/                   # HTML templates
│   └── prediction_results/          # Saved prediction outputs
│
├── tests/                           # Regression tests
│   ├── test_kronos_regression.py    # Numerical regression & MSE tests
│   └── data/                        # Test data (CSV + expected outputs)
│
├── my_predict/                      # (Empty) — user's custom prediction scripts
└── figures/                         # README images & diagrams
```

---

## Building and Running

### Installation

```bash
# Using pip
pip install -r requirements.txt

# Using uv (recommended if uv.lock is present)
uv sync
```

### Making Predictions

```python
from model import Kronos, KronosTokenizer, KronosPredictor

tokenizer = KronosTokenizer.from_pretrained("NeoQuasar/Kronos-Tokenizer-base")
model = Kronos.from_pretrained("NeoQuasar/Kronos-small")
predictor = KronosPredictor(model, tokenizer, max_context=512)

pred_df = predictor.predict(
    df=x_df,                    # DataFrame with [open, high, low, close, volume, amount]
    x_timestamp=x_timestamp,    # Historical timestamps
    y_timestamp=y_timestamp,    # Future timestamps
    pred_len=120,               # Number of steps to predict
    T=1.0,                      # Temperature
    top_p=0.9,                  # Nucleus sampling
    sample_count=1,             # Number of forecast paths
)
```

### Running Tests

```bash
# Regression tests (numerical reproducibility)
pytest tests/test_kronos_regression.py -v
```

### Running the Web UI

```bash
cd webui
python run.py
# Then visit http://localhost:7070
```

### Finetuning

**Via Qlib (A-share market):**
```bash
# 1. Prepare data
python finetune/qlib_data_preprocess.py

# 2. Finetune tokenizer (multi-GPU)
torchrun --standalone --nproc_per_node=NUM_GPUS finetune/train_tokenizer.py

# 3. Finetune predictor (multi-GPU)
torchrun --standalone --nproc_per_node=NUM_GPUS finetune/train_predictor.py

# 4. Backtest
python finetune/qlib_test.py --device cuda:0
```

**Via CSV (any market):**
```bash
# Edit configs/config_ali09988_candle-5min.yaml first, then:
cd finetune_csv
python train_sequential.py --config configs/config_ali09988_candle-5min.yaml
```

---

## Development Conventions

- **Model loading**: All models use Hugging Face `PyTorchModelHubMixin` for `from_pretrained()` / `save_pretrained()`.
- **Data format**: Input DataFrames must contain `['open', 'high', 'low', 'close']`; `volume` and `amount` are optional (filled with zeros if missing).
- **Context limit**: `Kronos-small` and `Kronos-base` have a max context of 512. `Kronos-mini` supports 2048. The predictor auto-truncates longer inputs.
- **Device**: Pass `device` to `KronosPredictor` (e.g., `"cpu"`, `"cuda:0"`, `"mps"`).
- **Finetuning config**: All paths and hyperparameters are centralized in `finetune/config.py` (Qlib pipeline) or YAML configs (CSV pipeline).
- **Distributed training**: Uses `torchrun` with `nccl` backend for multi-GPU finetuning.
- **Tests**: Regression tests compare numerical output against pre-computed expected CSVs with strict tolerances (`rtol=1e-5`). MSE tests verify average prediction error against known baselines.
- **Code style**: The project uses `einops` for tensor operations, `safetensors` for model serialization, and follows standard PyTorch `nn.Module` conventions.
