simple scritp to monitor cpu and hdd temperatures</br>
outputs the info to temps.json</br>

**Installation**</br>
`pip install -r requirements.txt`
(if needed use pip3)</br>
install package hddtemp:</br>
<Arch Linux></br>
`sudo pacman -S hddtemp`</br>
<Ubuntu/Debian></br>
`sudo apt-get install hddtemp`</br>

**How to run it**</br>
`crontab -e`</br>
`* * * * * python /path_to_script/script.py`</br>

