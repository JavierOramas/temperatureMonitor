from flask import Flask
import pandas as pd
from os import path
app = Flask(__name__)

@app.route('/')
def get_temps():
    return pd.read_json(path.join(path.dirname(path.abspath(__file__)),'data/temp.json'), lines=True, convert_dates=False, dtype=float).to_dict(orient='dict')
@app.route('/history')
def get_history():
    return pd.read_json(path.join(path.dirname(path.abspath(__file__)),'data/history.json'), lines=True, convert_dates=False, dtype=float).to_dict(orient='dict')


if __name__ == '__main__':
    app.run(debug=True)