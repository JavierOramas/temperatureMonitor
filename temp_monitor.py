import streamlit as st
import pandas
import psutil
from datetime import datetime
from os import getenv,path,system
from utils import list_disks,filter_date

system('python3 '+ path.join(path.dirname(path.abspath(__file__)),'script.py get_temperatures'))
st.title('Monitor de Temperatura')
df = pandas.read_json(path.join('data/temps.json'), lines=True)
df['cpu'] = df['Package id 0']


if st.sidebar.checkbox('Filtrar por fecha'):
    start = st.date_input(label='start')
    end = st.date_input(label='end')
    # start = 
    df = filter_date(df,start, end)

if st.sidebar.checkbox('show all data'):
    try:
        old = pandas.read_json(path.join('data/history.json'), lines=True)
        df = pandas.concat([old,df])
    except:
        pass
    df = df.reset_index(drop=True)
if st.button(label='Obtener valores actuales'):
    system('python3 '+ path.join(path.dirname(path.abspath(__file__)),'script.py get_temperatures'))

if st.button(label='Eliminar datos antiguos'):
    system('python3 '+ path.join(path.dirname(path.abspath(__file__)),'clean.py 100'))

if st.sidebar.checkbox('Mostrar datos de la CPU'):
    st.line_chart(df['cpu'], )

cores = []
for i in range(len(psutil.sensors_temperatures()['coretemp'])-1):
    cores.append('Core '+str(i)) 

cores_df = pandas.DataFrame(df,columns=cores)

# temps['disks'] = len(hdds)
if st.sidebar.checkbox("Show Core Details"):
    st.text('Cores')
    st.line_chart(cores_df)

if st.sidebar.checkbox("Show raw Data(cpu)"):
    df['cpu']
    cores_df


# temps['disks'] = len(hdds)
disks = list_disks()

if st.sidebar.checkbox('Mostrar datos de los discos'):
    st.text('Disks')
    for i in disks:
        st.line_chart(df[i])

if st.sidebar.checkbox("Show raw Data (disks)"):
    for i in disks:
        df[i]
#    date_day = st.sidebar.date_input("fecha",datetime.datetime.now(), key="daydate")
