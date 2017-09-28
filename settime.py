# This script connects to a datetime API in order to set system datetime automatically.
# A personal API key is used to fetch current datetime and it is set to get datetime for Cuba.
# Modifications can be made in order to get datetime for other zones. A full list of available zones can be found in https://timezonedb.com/time-zones
# Please consider registering for your own API key in https://timezonedb.com/register
# In order to change the system date in Linux, sudo privileges are required.
# To prevent the script from asking your password when executing `sudo date`, following line must be added to /etc/sudoers file:
# <user>    ALL=(ALL)    NOPASSWD:   /bin/date
# Remember to use `sudo visudo` to edit sudoers file.
# Also, consider executing this script every time at reboot, placing it in a given directory and adding a crontab with `crontab -e`
# @reboot python3 <script directory> &

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
    os.system('sudo date -s \'' + datetime + '\'')

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