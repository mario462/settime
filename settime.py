# Author: Mario Muniz <mario462@gmail.com>

#!/usr/bin/python3
import os
import sys
import datetime
from urllib.request import urlopen
import json

def parseDateTime(datetime):
    date_time = datetime.split()
    date = date_time[0].split('-')
    time = date_time[1].split(':')
    return { 'year': int(date[0]), 'month': int(date[1]), 'day': int(date[2]), 'hour': int(time[0]), 'minute': int(time[1]), 'second': int(time[2]) }

def getDateTime():
    res = urlopen('http://api.timezonedb.com/v2/get-time-zone?key=32K5LP2OEOTI&format=json&by=zone&zone=America/Havana').read().strip().decode()
    result = json.loads(res)
    return result['formatted']

def linuxSetTime(datetime):
    os.system('sudo /bin/date -s \'' + datetime + '\'')

def windowsSetTime(datetime):
    try:
        import pywin32
    except ImportError:
        print('pywin32 module is missing')
        sys.exit(1)
    parsed = parseDateTime(datetime)
    pywin32.SetSystemTime(parsed['year'], parsed['month'] , parsed['dayOfWeek'] , parsed['day'] , parsed['hour'] , parsed['minute'] , parsed['second'] , 0 )

if __name__ == '__main__':
    datetime = getDateTime()
    print('Setting time to ' + datetime)
    if sys.platform == 'linux':
        linuxSetTime(datetime)
    elif sys.platform == 'win32':
        windowsSetTime(datetime)