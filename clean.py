from json import dump
from os import path
import json
import sys
import pandas as pd
from utils import filter_date
from datetime import datetime

def clean(items_left=100):
    df = pd.read_json(path.join(path.dirname(path.abspath(__file__)),'data/temp.json'), lines=True, convert_dates=False, dtype=float)

    # df['date'] = [i for i in df['date']]
    ndf = pd.DataFrame(df.tail(items_left))
    df = df[:-items_left]
    
    filter_date(ndf,datetime(2020,6,25,23,0,0,0),datetime(2020,6,26,0,0,0,0))
    

    ndf.to_json(path.join(path.dirname(path.abspath(__file__)),'data/temp.json'), lines=True, orient='records')
    with open(path.join(path.dirname(path.abspath(__file__)),'data/temp.json'), 'a') as json_file:
        json_file.write('\n')

    if len(df) > 0:
        df.to_json(path.join(path.dirname(path.abspath(__file__)),'data/temporal.json'), orient='records', lines=True), 

        df = open(path.join(path.dirname(path.abspath(__file__)),'data/temporal.json'), 'r')
        with open(path.join(path.dirname(path.abspath(__file__)),'data/history.json'), 'a') as json_file:
            for i in df.readlines():
                json_file.write(i)
                if not i[-1] == '\n':
                    json_file.write('\n')


if __name__ == '__main__':
    clean(int(sys.argv[1]))