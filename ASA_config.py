from netmiko import ConnectHandler
import getpass
import sys
file = open('IP', 'r')

USER = input('Username: ')
PASSWORD = getpass.getpass()
ENABLE_PASS = getpass.getpass(prompt='Enter enable password: ')
DEVICES_IP = file.read().split('\n')
print(DEVICES_IP)

for line in DEVICES_IP:
    ip_address = line.strip()
    print(ip_address)
    device = {
        'device_type': 'cisco_asa',
        'ip': ip_address,
        'username': USER,
        'password': PASSWORD,
        'secret': ENABLE_PASS,
        'port': 22,
    }
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command('show access-list in_Factory | i deny ip any any')
    hostname = net_connect.send_command('show version')
    print(hostname, output)
    net_connect.disconnect()