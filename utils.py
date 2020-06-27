from os import popen
import pandas as pd
import datetime
import time

def list_disks():
    hdds = []
    for i in popen('lsblk -d'):
        temp = []
        i = i.replace('\n', '')
        for item in i.split(' '):
            if not item == '':
                temp.append(item)
        hdds.append(temp)

    list_hdds = []
    for i in hdds:
        if i[5] == 'disk':
            list_hdds.append(i[0])

    return list_hdds

def clean_digits(string):
    output = ''
    for i in string:
        try:
            num = int(i)
            output = output+i
        except:
            continue
    return output

def filter_date(df, start, end): 
    elems = []
    for i in df['date']:
        elems.append(start <= datetime.datetime.strptime(str(i),'%Y-%m-%d 00:00:00').date() <= end)
        df.reset_index()
    return df[elems]  