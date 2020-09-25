
from typer import Typer
import os
import shutil
import socket

app = Typer()


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip = 'localhost'
    try:
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except:
        ip = '127.0.0.1'
    return ip

@app.command(name='api', help='Installs temp monitor api as a service')
def install_api():
    
    unit = '''[Unit]\nDescription=API for the Temp Monitor app and webapp\nAfter=network.target\n'''
    service = '''\n[Service]\nUser={user}\nWorkingDirectory={dir}\nExecStart={gunicorn} -w 4 -b {ip}:9998 api:app\nRestart=always\n'''
    install = '''\n[Install]\nWantedBy=multi-user.target\n'''
    
    with open('/etc/systemd/system/temp_monitor_api.service', 'w') as file:
        service = service.replace('{user}', os.getlogin())
        service = service.replace('{dir}', os.path.dirname(os.path.abspath(__file__)))
        service = service.replace('{gunicorn}', shutil.which('gunicorn'))
        service  = service.replace('{ip}', get_ip())
        string = unit + service + install 
        file.write(string)

@app.command(name='webui', help='Installs temp monitor webui as a service')
def install_api():
    
    unit = '''[Unit]\nDescription=Temp Monitor webapp\nAfter=network.target\n'''
    service = '''\n[Service]\nUser={user}\nWorkingDirectory={dir}\nExecStart={streamlit} run temp_monitor.py --server.port 9999\nRestart=always\n'''
    install = '''\n[Install]\nWantedBy=multi-user.target\n'''
    
    with open('/etc/systemd/system/temp_monitor_web.service', 'w') as file:
        service = service.replace('{user}', os.getlogin())
        service = service.replace('{dir}', os.path.dirname(os.path.abspath(__file__)))
        service = service.replace('{streamlit}', shutil.which('streamlit'))
        string = unit + service + install 
        file.write(string)

if __name__ == '__main__':
    app()
