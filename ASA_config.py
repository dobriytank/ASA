from netmiko import ConnectHandler
import getpass
import time
import sys

file = open('IP', 'r')
USER = input('Username: ')
PASSWORD = getpass.getpass()
ENABLE_PASS = getpass.getpass(prompt='Enter enable password: ')
DEVICES_IP = file.read().splitlines()
print(DEVICES_IP)
file.close()
result = open('result', 'w')


for line in DEVICES_IP:
 #   if line[0] == "#": continue
    ip_address = line.strip()
    device = {
    'device_type': 'cisco_asa',
    'ip': ip_address,
    'username': USER,
    'password': PASSWORD,
    'secret': ENABLE_PASS,
    'port': 22,
    }
    net_connect = ConnectHandler(**device, global_delay_factor=2)
#    net_connect.config_mode()
    output = net_connect.send_command('show running-config | include access-group in_Office')
    time.sleep(2)
    hostname = net_connect.send_command('show hostname')

    if output!="":
        print(hostname, ip_address, output)
        result.write(hostname + ip_address+'\n' + output+'\n')
    else:
        print(hostname, 'No such string')
        result.write(hostname + ip_address+'\n' + 'No such string'+'\n')
    net_connect.disconnect()
    time.sleep(2)

result.close()
