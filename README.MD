simple scritp to monitor cpu and hdd temperatures in lunix
outputs the info to temps.json

**Installation**
`pip install -r requirements.txt`
(if needed use pip3)

-install package hddtemp:
<Arch Linux>
`sudo pacman -S hddtemp`
<Ubuntu/Debian>
`sudo apt-get install hddtemp`

**How to run it**
`crontab -e`
`* * * * * python /path_to_script/script.py`
