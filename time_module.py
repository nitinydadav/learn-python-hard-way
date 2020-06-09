from time import time, ctime, localtime

sec = time()
print(sec)

dmt = ctime(sec)

print("current date mon time ", ctime())  # this will give you current date & time.

print("Date -mon - time - sec ", (dmt))

obj = localtime()
print(obj)
print("day ", "=", obj.tm_mday)
print("month ", "=", obj.tm_mon)
print("year ", "=", obj.tm_year)
print("hour ", "=", obj.tm_hour)
print("min ", "=", obj.tm_min)

print('\n')

from datetime import datetime

dt = datetime(year=2020, month=3, day=30)
print(dt)
dt1 = datetime(year=2020, month=3, day=30, hour=11, minute=50)
print(dt1)

dt2 = datetime(2020, 3, 30, 11, 50)
print(dt2)

from threading import Thread


def num():
    for i in range(5):
        print("child Thread")
y = Thread(target=num)


print(y.start())

for i in range(5):
    print("main Thread")
