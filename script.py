import psutil
from os import popen
from json import dump
import datetime
# def get_cpu_temps():
temps = {}
temps['date'] = str(datetime.datetime.now())

for i in psutil.sensors_temperatures()['coretemp']:
    temps[i[0]] = i[1]


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
for i in list_hdds:
    text = str(popen('hddtemp /dev/'+i).read())
    if text == '':
        text = 'sleeping'
    else:
        text = text.split(': ')[-1].replace('\u00b0C\n', '')

    temps[i] = text
    
with open('temp.json', 'a') as json_file:
    dump(temps, json_file)    