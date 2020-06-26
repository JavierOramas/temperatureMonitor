import streamlit as st
import pandas
import psutil
from os import getenv,path,system
from utils import list_disks


df = pandas.read_json(path.join('data/temp.json'), lines=True)

if st.checkbox('show all data'):
    old = pandas.read_json(path.join('data/history.json'), lines=True)
    df = pandas.concat([old,df])
    df = df.reset_index(drop=True)
if st.button(label='Obtener valores actuales'):
    system('python3 '+ path.join(path.dirname(path.abspath(__file__)),'script.py'))


df['cpu'] = df['Package id 0']
st.line_chart(df['cpu'], )

cores = []
for i in range(len(psutil.sensors_temperatures()['coretemp'])-1):
    cores.append('Core '+str(i))    

cores_df = pandas.DataFrame(df,columns=cores)

# temps['disks'] = len(hdds)
if st.checkbox("Show Core Details"):
    st.text('Cores')
    st.line_chart(cores_df)

if st.checkbox("Show raw Data(cpu)"):
    df['cpu']
    cores_df


# temps['disks'] = len(hdds)
st.text('Disks')
disks = list_disks()

for i in disks:
    st.line_chart(df[i])

if st.checkbox("Show raw Data (disks)"):
    for i in disks:
        df[i]
