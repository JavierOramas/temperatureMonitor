
from typer import Typer
import os
import shutil

app = Typer()

@app.command(name='API', help='Installs temp monitor api as a service')
def install_api():
    
    unit = '''[Unit]\nDescription=API for the Temp Monitor app and webapp\nAfter=network.target\n'''
    service = '''\n[Service]\nUser={user}\nWorkingDirectory={dir}\nExecStart={gunicorn} api:app\nRestart=always\n'''
    install = '''\n[Install]\nWantedBy=multi-user.target\n'''
    
    with open('/etc/systemd/system/temp_monitor_api.service', 'w') as file:
        service = service.replace('{user}', os.getlogin())
        service = service.replace('{dir}', os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        service = service.replace('{gunicorn}', shutil.which('gunicorn'))
        string = unit + service + install 
        file.write(string)

if __name__ == '__main__':
    app()
