import psutil
from json import dump
from os import getenv,path,popen
import datetime
from utils import list_disks,clean_digits
import string
# def get_cpu_temps():
temps = {}
temps['date'] = str(datetime.datetime.now())

for i in psutil.sensors_temperatures()['coretemp']:
    temps[i[0]] = i[1]


list_hdds = list_disks()

for i in list_hdds:
    text = str(popen('sudo hddtemp /dev/'+i).read())
    if text == '':
        text = '0'
    else:
        text = text.split(': ')[-1].replace('\u00b0C\n', '')
        text = clean_digits(text)
    temps[i] = text

home = getenv("HOME")
with open(path.join(path.dirname(path.abspath(__file__)),'data/temp.json'), 'a') as json_file:
    dump(temps, json_file)   
    json_file.write('\n') 
    