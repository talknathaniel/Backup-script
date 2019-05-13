from datetime import datetime, timedelta
from threading import Timer
import os
import time
os.system("cls")
x=datetime.today()
y = x.replace(day=x.day, hour=19, minute=30, second=0, microsecond=0) + timedelta(days=1)
delta_t=y-x

secs=delta_t.total_seconds()

def hello_world():
    os.system("python start.py")


t = Timer(secs, hello_world)
t.start()
t.join()