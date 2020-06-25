import psutil
from json import dump
import datetime
# def get_cpu_temps():
cpu = {}
for i in psutil.sensors_temperatures()['coretemp']:
    cpu[i[0]] = i[1]

cpu['date'] = str(datetime.datetime.now())

with open('temp.json', 'a') as json_file:
    dump(cpu, json_file)    