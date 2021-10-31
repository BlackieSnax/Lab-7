import os
from netmiko import ConnectHandler
from getpass import getpass
from netmiko.ssh_exception import AuthenticationException, SSHException, NetmikoTimeoutException

USERNAME = input("Please enter your SSH username: ")
PASS = getpass ("Please enter your SSH password: ")

device = {
    'ip': '192.168.108.11',
    'username': USERNAME,
    'password': PASS,
    'device_type': 'cisco_ios'
}

try:
 c = ConnectHandler(**device)
 output = c.send.send_command('show run')
 f = open('backup.conf', 'x')
 f.write(output)
 f.close()

except (NetmikoTimeoutException):
 print("The device " + device['ip'] + " timed out when attempting to connect")

except (AuthenticationException):
 print("An authentication error occured while trying to connect to: " + device['ip'])

except (SSHException):
 print("An error occured while connecting to device " + device['ip'] + " via SSH. Is SSH enabled?")
