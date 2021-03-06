import psutil
from json import dump
from os import getenv,path,popen
import datetime
from utils import list_disks,clean_digits
import string
import typer

app = typer.Typer()

def get_date():
    return str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def export_json(file, name):
    home = getenv("HOME")
    print()
    with open(path.join(path.dirname(path.abspath(__file__)),'data/'+name+'.json'), 'a') as json_file:
        dump(file, json_file)   
        json_file.write('\n') 

@app.command(name='get_temperatures', help='generate or add to a json the actual temperatures from the cpu and hdds')
def get_temperatures():
    temps = {}
    temps['date'] = get_date()

    for i in psutil.sensors_temperatures()['coretemp']:
        temps[i[0]] = i[1]


    list_hdds = list_disks()

    for i in list_hdds:
        try:
            text = str(popen('sudo hddtemp /dev/'+i).read())
            
            if text == '' or 'ERROR' in text:
                text = 0.0
            else:
                text = text.split(': ')[-1].replace('\u00b0C\n', '')
                text = float(clean_digits(text))
            temps[i] = text
        except:
            pass
    # print(temps)
    export_json(temps, 'temps')

@app.command(name='get_cpu_usage', help='generate or add to a json the actual cpu usage percent')
def get_cpu_load():
    usage = {}
    usage['date'] = get_date()
    usage['cpu'] = psutil.cpu_percent()
    # usage['stats'] = psutil.cpu_times()
    export_json(usage, 'cpu_usage')

@app.command(name='get_memory_usage', help='generate or add to a json the actual memory usage and memory usage percent')
def get_memory_usage():
    memory = {}
    memory['date'] = get_date()
    memory['swap'] = psutil.swap_memory()
    memory['phisical'] = (psutil.virtual_memory().total - psutil.virtual_memory().available) / 1000000000
    memory['precentage'] = (memory['phisical'] / ( psutil.virtual_memory().total / 1000000000 ) ) * 100

    export_json(memory, 'memory_usage')
    

if __name__ == "__main__":
    app()
