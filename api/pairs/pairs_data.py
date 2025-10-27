from time import sleep
import pandas as pd
import json
from api.data.data import ExternalData

class PairsData:

    @staticmethod
    def create_pairs_json(pair_1_symbol, pair_2_symbol, interval, beta, lag, high_sigma, low_sigma):
        pair_1_df = ExternalData.get_candles(pair_1_symbol, interval)
        sleep(0.1)
        pair_2_df = ExternalData.get_candles(pair_2_symbol, interval)
        pairs_df = pd.merge(pair_1_df, pair_2_df, on='time', suffixes=[pair_1_symbol, pair_2_symbol])
        pairs_df['spread'] = pairs_df[f'close{pair_1_symbol}'] - beta * pairs_df[f'close{pair_2_symbol}']
        pairs_df['z'] = (pairs_df['spread'] - pairs_df['spread'].rolling(lag).mean()) / pairs_df['spread'].rolling(lag).std()
        pairs_df.dropna(inplace=True)
        pairs_df['time'] = pairs_df.index.strftime('%Y-%m-%d %H:%M:%S')
        pairs_df = pairs_df[['time', 'spread', 'z']]
        pairs_df['cross_up_sigma'] = ((pairs_df['z'] > high_sigma) & (pairs_df['z'] > pairs_df['z'].shift(1)) & (pairs_df['z'].shift(1) < high_sigma))
        pairs_df['cross_down_sigma'] = ((pairs_df['z'] < low_sigma) & (pairs_df['z'] < pairs_df['z'].shift(1)) & (pairs_df['z'].shift(1) > low_sigma))
        pairs_df['cross_up_zero'] = ((pairs_df['z'] > 0) & (pairs_df['z'] > pairs_df['z'].shift(1)) & (pairs_df['z'].shift(1) < 0) & (pairs_df['z'].shift(1) < 0))
        pairs_df['cross_down_zero'] = ((pairs_df['z'] < 0) & (pairs_df['z'] < pairs_df['z'].shift(1)) & (pairs_df['z'].shift(1) > 0) & (pairs_df['z'].shift(1) < 0))
        pairs_df.dropna(axis=1, inplace=True)
        return pairs_df.to_json(orient='records')