# settime
This script connects to a datetime API in order to set system datetime automatically.

A personal API key is used to fetch current datetime and it is set to get datetime for Cuba.
Modifications can be made in order to get datetime for other zones. A full list of available zones can be found in https://timezonedb.com/time-zones

Please consider registering for your own API key in https://timezonedb.com/register

In order to change the system date in Linux, sudo privileges are required.
To prevent the script from asking your password when executing ```sudo date```, following line must be added to /etc/sudoers file:

    <user>    ALL=(ALL)    NOPASSWD:   /bin/date

Remember to use ```sudo visudo``` to edit sudoers file.

Also, consider executing this script every time at reboot, placing it in a given directory and adding a crontab with ```crontab -e```:

    @reboot python3 <script directory> &
