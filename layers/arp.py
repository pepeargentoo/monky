from struct import pack,unpack
from socket import inet_aton
from binascii import unhexlify,hexlify
import socket

opcode_type ={
	'ARP_REQUEST':1,
	'ARP_REPLY':2
}

hard_type = {
	'ETHERNET':1,
	'802NETWORK':6,
	'ARCNET':7,
	'FRAME_RELAY':15,
	'ATM':16,
	'HDLC':17,
	'FIBER_CHANELL':18,
	'ATM_':19,
	'SERIAL':20
}

class ARP(object):
	def __init__(self):
		self.hard_type = ''
		self.proto_type = 0x0800
		self.hard_len = 6
		self.proto_len = 4
		self.opcode = ''
		self.src_ip = ''
		self.src_mac = ''
		self.dst_ip =''
		self.dst_mac = ''

	def create(self):
		self.src_ip = inet_aton(self.src_ip)
		self.dst_ip = inet_aton(self.dst_ip)
		self.send_src_mac = unhexlify(self.src_mac.replace(":","")) 
		self.send_dst_mac = unhexlify(self.dst_mac.replace(":",""))

		return pack('!HHBBH6s4s6s4s',self.hard_type,self.proto_type,self.hard_len,self.proto_len,self.opcode,self.send_src_mac,self.src_ip,self.send_dst_mac,self.dst_ip )
	
	def get_response(self):

		sock_arp = socket.socket( socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0003))
		packet = sock_arp.recvfrom(2048)
		ethernet_header = packet[0][0:14]
		header_arp = unpack("!6s6s2s", ethernet_header)
		arp_header = packet[0][14:42]
		body_arp = unpack("2s2s1s1s2s6s4s6s4s", arp_header)
		
		arp_dest = hexlify(header_arp[0])
		arp_src = hexlify(header_arp[1])
		
		arp_dst = arp_dest[0:2]+':'+arp_dest[2:4]+':'+arp_dest[4:6]+':'+arp_dest[6:8]+':'+arp_dest[8:10]+':'+arp_dest[10:12]
		arp_src = arp_src[0:2]+':'+arp_src[2:4]+':'+arp_src[4:6]+':'+arp_src[6:8]+':'+arp_src[8:10]+':'+arp_src[10:12]

		if(self.src_mac == arp_dst):
			mac_dst = hexlify(body_arp[5])
			mac_dst =  mac_dst[0:2]+':'+mac_dst[2:4]+':'+mac_dst[4:6]+':'+mac_dst[6:8]+':'+mac_dst[8:10]+':'+mac_dst[10:12]
			return mac_dst
		else:
			self.get_response()
	
class ARPRequest(ARP):
	def __init__(self):
		ARP.__init__(self)
		self.opcode = 1
		self.hard_type = 1

	def create(self):
		return ARP.create(self)

	def response(self):
		sock_arp = socket.socket( socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0003))
		packet = sock_arp.recvfrom(2048)
		ethernet_header = packet[0][0:14]
		header_arp = unpack("!6s6s2s", ethernet_header)
		arp_header = packet[0][14:42]
		body_arp = unpack("2s2s1s1s2s6s4s6s4s", arp_header)
		
		arp_dest = hexlify(header_arp[0])
		arp_src = hexlify(header_arp[1])
		
		arp_dst = arp_dest[0:2]+':'+arp_dest[2:4]+':'+arp_dest[4:6]+':'+arp_dest[6:8]+':'+arp_dest[8:10]+':'+arp_dest[10:12]
		arp_src = arp_src[0:2]+':'+arp_src[2:4]+':'+arp_src[4:6]+':'+arp_src[6:8]+':'+arp_src[8:10]+':'+arp_src[10:12]
		ip_dst = socket.inet_ntoa(body_arp[8])
		#print(hexlify(body_arp[5]))
		if(self.src_mac == arp_dst and socket.inet_ntoa(self.src_ip) == ip_dst):
			mac_dst = hexlify(body_arp[5])
			mac_dst =  mac_dst[0:2]+':'+mac_dst[2:4]+':'+mac_dst[4:6]+':'+mac_dst[6:8]+':'+mac_dst[8:10]+':'+mac_dst[10:12]
			return mac_dst
		else:
			self.get_response()

class ARPRepley(ARP):
	def __init__(self):
		ARP.__init__(self)
		self.opcode = 2
		self.hard_type = 1
	def create(self):
		return ARP.create(self)
		