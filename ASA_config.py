from netmiko import ConnectHandler
import getpass
import sys

file = open('IP', 'r')


USER = input('Username: ')
PASSWORD = getpass.getpass()
ENABLE_PASS = getpass.getpass(prompt='Enter enable password: ')
DEVICES_IP = file.read().split('\n')
print(DEVICES_IP)

