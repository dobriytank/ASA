from netmiko import ConnectHandler
import getpass
import sys

file = open('IP', 'r')

USER = input('Username: ')
PASSWORD = getpass.getpass()
ENABLE_PASS = getpass.getpass(prompt='Enter enable password: ')
DEVICES_IP = ['10.78.16.4','10.78.16.4']

for IP in DEVICES_IP:
    print('Connection to device {}'.format(IP))
    DEVICE_PARAMS = {'device_type': 'cisco_asa',
                     'ip': IP,
                     'username': USER,
                     'password': PASSWORD,
                     'secret': ENABLE_PASS}

    with ConnectHandler(**DEVICE_PARAMS) as ssh:
        ssh.enable()

        #result = ssh.send_command(COMMAND)
        #print(result)
