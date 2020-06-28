Simple scritp to monitor cpu and hdd temperatures</br>
Currently does not have support for multi CPU systems</br>
outputs the info to temps.json</br>


**Installation**</br>
`pip install -r requirements.txt`
(if needed use pip3)</br>
install package hddtemp:</br>
*Arch Linux*</br>
`sudo pacman -S hddtemp`</br>
*Ubuntu/Debian*</br>
`sudo apt-get install hddtemp`</br>

add the following line to the sudoers file (`sudo visudo`)
`{USER} ALL= NOPASSWD: /usr/bin/hddtemp`

**How to run it**</br>
`crontab -e`</br>
`10 * * * * python /path_to_folder/script.py`</br> 
(change crontab setting to modify run frequency)</br>

**Web Interface**</br>
set the following command to run at startup and set the port of your preference</br>
`streamlit run /path_to_folder/webui.py --server.port {port}`</br>

**For Cleaning the Data**</br>
In order to avoid excess of info, you can run the clean.py script to leave only the last X elements (default:100)</br>
`python3 clean.py X`</br>

**API**
set the following command to run at startup, set the port inside</br>
`streamlit run /path_to_folder/webui.py --server.port {port}`</br>