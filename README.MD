[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FJavierOramas%2temperatureMonitor&count_bg=%233D91C8&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

Simple scritp to monitor cpu and hdd temperatures</br>
Currently does not have support for multi CPU systems</br>
outputs the info to temps.json</br>


# Installation
`pip install -r requirements.txt`
(if needed use pip3)</br>
install package hddtemp:</br>
*Arch Linux*</br>
`sudo pacman -S hddtemp`</br>
*Ubuntu/Debian*</br>
`sudo apt-get install hddtemp`</br>

add the following line to the sudoers file (`sudo visudo`)
`{USER} ALL= NOPASSWD: /usr/bin/hddtemp`

# How to run it
`crontab -e`</br>
`10 * * * * python /path_to_folder/script.py`</br> 
(change crontab setting to modify run frequency)</br>

# Deploy to a Server
to deploy to a server you have to run:
`sudo python3 setup.py [ api|webui ]`
`sudo systemctl daemon-reload`

`sudo systemctl enable temp_monitor_api` or
`sudo systemctl enable temp_monitor_web`

`sudo systemctl start temp_monitor_api` or
`sudo systemctl start temp_monitor_web`

this will make the services start with the system

# Web Interface
set the following command to run at startup and set the port of your preference</br>
`streamlit run /path_to_folder/webui.py --server.port {port}`</br>

## For Cleaning the Data
In order to avoid excess of info, you can run the clean.py script to leave only the last X elements (default:100)</br>
`python3 clean.py X`</br>

# API
set the following command to run at startup, set the port inside</br>
`streamlit run /path_to_folder/webui.py --server.port {port}`</br>

# Inside the code

## fetching the data

to get the data manually you have to run:</br>
`python script.py <option>`

### get_temperatures
this command gets the temperature from the cpu and hdd's and dumps it to data/temps.json

### get_cpu_usage (alpha)
this command gets the cpu usage percent and dumps it to /data/cpu_usage.json

### get_memory_usage (alpha)
this command gets the memory usage percent and actual memory usage ammount and dumps it to /data/memory_usage.json
