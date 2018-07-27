from netmiko import ConnectHandler
import getpass
import sys
file = open('IP', 'r')

USER = input('Username: ')
PASSWORD = getpass.getpass()
ENABLE_PASS = getpass.getpass(prompt='Enter enable password: ')
DEVICES_IP = file.read().split('\n')
print(DEVICES_IP)
file.close()
result = open('result', 'w')

for line in DEVICES_IP:
    ip_address = line.strip()
 #   print(ip_address)
    device = {
        'device_type': 'cisco_asa',
        'ip': ip_address,
        'username': USER,
        'password': PASSWORD,
        'secret': ENABLE_PASS,
        'port': 22,
    }
    net_connect = ConnectHandler(**device)
#    net_connect.config_mode()
    output = net_connect.send_command('show run | i access11111')
    hostname = net_connect.send_command('show hostname')

    if output!="":
        print(hostname, ip_address, output)
        result.write(hostname + ip_address+'\n' + output+'\n')
    else:
        print(hostname, 'No such string')
        result.write(hostname + 'No such string'+'\n')
    net_connect.disconnect()

result.close()
#def write_to_file(multiple, output_file, input_parse, input_names, input_objects, input_object_groups,
 #                     input_access_lists, input_object_nat, input_static_nat, ip_address):
#
 #       if multiple:
  #          filename = ip_address.split('.')[0] + "-" + ip_address.split('.')[1] + "-" + ip_address.split('.')[
   #             2] + "-" + ip_address.split('.')[3] + ".txt"
    #        f = open(filename, 'w')
     #   else:
      #      if output_file:
       #         f = open(output_file, 'w')
        #    else:
         #       f = open("output.txt", 'w')
    #    f.write("Output returned for asa_ip.py script\n")
     #   f.write("IP Address Provided:  " + ip_address + "\n")
      #  f.write("Date:  " + today.ctime() + "\n\n\n")