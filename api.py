from flask import Flask
import pandas as pd
from os import path
import psutil
app = Flask(__name__)

@app.route('/temps')
def get_temps():
    json_file = pd.read_json(path.join(path.dirname(path.abspath(__file__)),'data/temp.json'), lines=True, convert_dates=False, dtype=float).to_dict(orient='dict')
    json_file['n_cores'] = len(psutil.sensors_temperatures()['coretemp'])-2
    return json_file
    # return pd.read_json(path.join(path.dirname(path.abspath(__file__)),'data/temp.json'), lines=True, convert_dates=False, dtype=float).to_dict(orient='dict')

@app.route('/history')
def get_history():
    return pd.read_json(path.join(path.dirname(path.abspath(__file__)),'data/history.json'), lines=True, convert_dates=False, dtype=float).to_dict(orient='dict')


if __name__ == '__main__':
    app.run(host='localhost', port=9998)
    #change host and port to the values you find convenient
    