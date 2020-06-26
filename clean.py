from json import dump
import json
import sys
import pandas as pd
from datetime import datetime

def clean(items_left=100):
    df = pd.read_json('data/temp.json', lines=True, convert_dates=False, dtype=float)

    # df['date'] = [i for i in df['date']]
    ndf = pd.DataFrame(df.tail(items_left))
    df = df[:-items_left]

    ndf.to_json('data/temp.json', lines=True, orient='records')
    with open('data/temp.json', 'a') as json_file:
        json_file.write('\n')

    if len(df) > 0:
        df.to_json('data/temporal.json', orient='records', lines=True), 

        df = open('data/temporal.json', 'r')
        with open('data/history.json', 'a') as json_file:
            for i in df.readlines():
                json_file.write(i)


if __name__ == '__main__':
    clean(int(sys.argv[1]))