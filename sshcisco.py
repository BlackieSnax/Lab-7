#Script to connect to Cisco devices via ssh prints to the linux terminal.
'''
import os
from netmiko import ConnectHandler
from getpass import getpass

USERNAME = input("Please enter your SSH username: ")
PASS = getpass ("Please enter your SSH password: ")

device = {
    'ip': '192.168.108.11',
    'username': USERNAME,
    'password': PASS,
    'device_type': 'cisco_ios'
}

c = ConnectHandler(**device)

output = c.send_command('show run')

print(output)
'''
#Script to connect to Cisco devices via ssh prints to the backup.conf

f = open('backup.conf', 'x')

import os
from netmiko import ConnectHandler
from getpass import getpass

USERNAME = input("Please enter your SSH username: ")
PASS = getpass ("Please enter your SSH password: ")

device = {
    'ip': '192.168.108.11',
    'username': USERNAME,
    'password': PASS,
    'device_type': 'cisco_ios'
}

c = ConnectHandler(**device)

output = c.send_command('show run')

f.write(output)
f.close()
