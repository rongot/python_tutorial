import sys
import calendar
import platform
from datetime import datetime,date
def version():
    print(f"python version:{sys.version}")
    print(f"today is {datetime.today().strftime('%Y-%m-%d')}")
    print(date.today())

version()
# calculate the number of days between two dates.
def calcNumberOfDays(date1:date,date2:date)->int:
    number=date1-date2
    print(number)
# print(calendar.month(2023,7))
date9="2014, 7, 2", (2014, 7, 11)

# def validateObject(x:int,y:int):
#         if isinstance(y,int) and isinstance(x,int):
#             return (x + y) * (x + y)
#         return False

print(platform.architecture())
print(platform.release())












