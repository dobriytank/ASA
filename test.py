device = {
    'device_type': 'cisco_asa',
    'ip': ip_address,
    'username': USER,
    'password': PASSWORD,
    'port': 22,
}

net_connect = ConnectHandler(**device)
output = net_connect.send_command_expect('show version')
print output