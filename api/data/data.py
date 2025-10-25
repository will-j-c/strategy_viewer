import pandas as pd
import requests as re

class ExternalData:

    @staticmethod
    def _public_query(url):
        res = re.get(url)
        return res.json()

    @staticmethod
    def _get_resolution_string(interval):
        if interval == 1:
            return '1m'
        if interval == 5:
            return '5m'
        if interval == 15:
            return '15m'
        if interval == 30:
            return '30m'
        if interval == 60:
            return '1h'
        if interval == 240:
            return '4h'
        if interval == 720:
            return '12h'
        if interval == 1440:
            return '1d'
        if interval == 10080:
            return '1w'
    
    @staticmethod
    def get_candles(symbol, interval):
        resolution = ExternalData._get_resolution_string(interval)
        url = f'https://demo-futures.kraken.com/api/charts/v1/trade/{symbol}/{resolution}'
        res = ExternalData._public_query(url)
        if 'candles' in res:
            if res['candles']:
                    ohlcv = ExternalData._create_df(res['candles'])
                    return ohlcv
    @staticmethod
    def get_market_price_tickers(self):
        url = 'https://futures.kraken.com/derivatives/api/v3/tickers'
        res = ExternalData._public_query(url)    
        df = pd.DataFrame.from_records(res['tickers'])
        return df[['symbol', 'markPrice']]
        
    @staticmethod
    def _create_df(candles):
        df = pd.DataFrame(candles)
        df['time'] = pd.to_datetime(df['time'], unit='ms')
        df.set_index(df['time'], inplace=True)
        df.drop('time', axis=1, inplace=True)
        df[['open', 'high', 'low', 'close', 'volume']] = df[[
            'open', 'high', 'low', 'close', 'volume']].astype(float)
        return df
