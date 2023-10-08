import psutil
import time

def log(content):
    with open("logs\log-usage.txt", "a") as file:
        file.write(content + "\n")

c = 0

time.sleep(10)
while(True):
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    memory_percent = memory_info.percent
    log(f"CPU: {cpu_percent}%, Memory: {memory_percent}%")
    time.sleep(1)
    c+=1
    if c == 60:
        break

