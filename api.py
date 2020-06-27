from flask import Flask
import pandas as pd
from os import path
app = Flask(__name__)

@app.route('/')
def dummy_api():
    return pd.read_json(path.join(path.dirname(path.abspath(__file__)),'data/temp.json'), lines=True, convert_dates=False, dtype=float).to_dict(orient='dict')
if __name__ == '__main__':
    app.run(debug=True)