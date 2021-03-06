from flask import Flask
import pandas as pd
from os import path, popen, system
from utils import list_disks
import psutil
app = Flask(__name__)

#TODO make a god home Page
@app.route('/')
def root():
    return 'temp_monitor_api'

@app.route('/temps')
def get_temps():
    system('python3 '+ path.join(path.dirname(path.abspath(__file__)),'script.py'))
    json_file = pd.read_json(path.join(path.dirname(path.abspath(__file__)),'data/temps.json'), lines=True, convert_dates=False, dtype=float).to_dict(orient='dict')
    json_file['n_cores'] = len(psutil.sensors_temperatures()['coretemp'])-2
    json_file['disks_name'] = list_disks()
    return json_file
    # return pd.read_json(path.join(path.dirname(path.abspath(__file__)),'data/temp.json'), lines=True, convert_dates=False, dtype=float).to_dict(orient='dict')

@app.route('/history')
def get_history():
    json_file = pd.read_json(path.join(path.dirname(path.abspath(__file__)),'data/history.json'), lines=True, convert_dates=False, dtype=float).to_dict(orient='dict')
    json_file['n_cores'] = len(psutil.sensors_temperatures()['coretemp'])-2
    json_file['disks_name'] = list_disks()
    return json_file

@app.route('/measure')
def measure():
    system('python3 '+ path.join(path.dirname(path.abspath(__file__)),'script.py get_temperatures'))
    system('python3 '+ path.join(path.dirname(path.abspath(__file__)),'script.py get_cpu_load'))
    return "OK"
    
@app.route('/clean')
def clean():
    system('python3 '+ path.join(path.dirname(path.abspath(__file__)),'clean.py')+' 100')
    return "OK"
    

if __name__ == '__main__':
    try:
        #change wlo1 to your network adapter's name
        try:
            ipv4 = popen('ip addr show lo').read().split("inet ")[1].split("/")[0]
            app.run(host=ipv4, port=9997)
        except:
            app.run(port=9997)
        #change host and port to the values you find convenient
    except:
        print("The network interface is not detected or not connected, \n please check network connection or changhe interface name in api.py" )