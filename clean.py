from json import dump
from os import path, remove
import json
import sys
import pandas as pd
from utils import filter_date
from datetime import datetime

def clean(items_left=100):
    files = ['data/temps.json','data/memory_usage.json', 'data/cpu_usage.json']

    for i in files:
        df = pd.read_json(path.join(path.dirname(path.abspath(__file__)),i), lines=True, convert_dates=False, dtype=float)

        # df['date'] = [i for i in df['date']]
        if (len(df) < items_left):
            continue

        ndf = pd.DataFrame(df.tail(items_left))
        df = df[:-items_left]    

        ndf.to_json(path.join(path.dirname(path.abspath(__file__)),i), lines=True, orient='records')
        with open(path.join(path.dirname(path.abspath(__file__)),i), 'a') as json_file:
            json_file.write('\n')

        # if len(df) > 0:
        #     df.to_json(path.join(path.dirname(path.abspath(__file__)),'data/temporal.json'), orient='records', lines=True), 

        #     df = open(path.join(path.dirname(path.abspath(__file__)),'data/temporal.json'), 'r')
        #     with open(path.join(path.dirname(path.abspath(__file__)),'data/history.json'), 'a') as json_file:
        #         for i in df.readlines():
        #             json_file.write(i)
        #             if not i[-1] == '\n':
        #                 json_file.write('\n')

        #     remove(path.join(path.dirname(path.abspath(__file__)),'data/temporal.json'))
if __name__ == '__main__':
    clean(int(sys.argv[1]))