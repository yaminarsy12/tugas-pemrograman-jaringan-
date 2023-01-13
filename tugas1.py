import socket
from binascii import hexlify
import re

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
def convert_ip4():
    list_ip =  ['127.0.0.1', '192.168.0.1','0.0.0.0','192.168.0.256','192.168.0.025', '258.168.1.1']
    for ip_addr in list_ip:
        print("IP Adress:", ip_addr)
        if (re.search(regex, ip_addr)):
            print("Status   : valid ip adress")
            packed_ip_addr = socket.inet_aton(ip_addr)
            unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
            print ("Ip : {} => Packed: {}, unpacked:{}".format(ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr))
        else:
            print("Status : invalid ip")
     

convert_ip4()
