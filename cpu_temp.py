from os import popen
import psutil

def get_cpu_temps():
    temps = popen('sensors').read()

    core_count = psutil.cpu_count(logical=False)

    temps = temps.split('\n')

    for i,item in enumerate(temps):
        if 'Package id 0:' in item:
            idx = i

    cpu_temp = temps[idx]
    cpu_cores = []

    for i in range(core_count):
        cpu_cores.append(temps[idx+i+1])
        
    return cpu_temp,cpu_cores

f = open('temps.txt', 'a')
cpu,cores = get_cpu_temps()
f.write(cpu+'\n')
for i in cores:
    f.write(i+'\n')