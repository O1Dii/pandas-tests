import pandas as pd


def sum():
    df = pd.read_csv('df')

    df['3'] = df['1'] + df['2']
    return df
