from xtquant import xtdata
import pandas as pd
from datetime import datetime, timedelta
import time


def _get_data_from_cache(symbols, startdate, enddate=datetime.today(), interval='5m'):
    dfs = xtdata.get_market_data_ex(
        stock_list=symbols,
        start_time=startdate.strftime('%Y%m%d%H%M%S'), # 格式为 %Y%m%d 或 %Y%m%d%H%M%S
        end_time=enddate.strftime('%Y%m%d%H%M%S'),     # 格式为 %Y%m%d 或 %Y%m%d%H%M%S
        period=interval,
        field_list=['time', 'open', 'high', 'low', 'close', 'volume'], # 指定需要的字段
        dividend_type = "front_ratio"  # 要跑实盘, 只能前复权
    )
    return dfs

        
def get_data_from_xtdata(symbols, startdate, enddate=datetime.today(), interval='5m'):
    '''
    开始结束日期需要是交易日, 否则会触发一次下载, 额外等待2秒.
    return:
    {"515310.SH":df}
    '''
    
    dfs = _get_data_from_cache(symbols, startdate, enddate, interval)
    need_download = False
    for symbol in symbols:
        indexs = '|'.join(str(ins) for ins in dfs[symbol].index)
        if (startdate.strftime('%Y%m%d') not in indexs) or (enddate.strftime('%Y%m%d') not in indexs):
            need_download = True
            break
    if need_download:
        # 先下载数据到本地缓存
        download_result = xtdata.download_history_data2(
            stock_list=symbols,
            period=interval,
            start_time=startdate.strftime('%Y%m%d%H%M%S'),
            end_time=enddate.strftime('%Y%m%d%H%M%S'),
            incrementally=True  # 增量下载模式[2,5](@ref)
        )
        
        time.sleep(2)
        dfs = _get_data_from_cache(symbols, startdate, enddate, interval)
        
    for symbol, df in dfs.items():
        # 标准化时间处理
        df['datetime'] = pd.to_datetime(df['time'], unit='ms', utc=True).dt.tz_convert('Asia/Shanghai')
        df.set_index('datetime', inplace=True)
        df.drop(columns=['time'], inplace=True)
        
    return dfs
        
        
if __name__ == '__main__':
    dfs = get_data_from_xtdata(
        # symbols=['515080.SH', '513100.SH', '518880.SH', '511220.SH'],
        symbols= ['NDX.US'],
        startdate=datetime.now() -timedelta(days=360*4),
        enddate=datetime.now()-timedelta(days=360*1),
        interval='1d'
    )
    print(dfs)