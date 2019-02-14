from struct import pack
from binascii import unhexlify

ether_type = {
	'IPv4':0x0800,
	'ARP': 0x0806,
	'WakeonLAN':0x0842,
	'IETFTRILL':0x22F3,
	'Stream_Reservation_Protocol':0x22EA,
	'DECnet':0x6003,
 	'RARP':0x8035,
 	'Ethertalk':0x809B,
 	'AARP':0x80F3,
 	'VLAN':0x8100,
 	'IPX':0x8137,
 	'QNX_Qnet':0x8204,
 	'IPv6':0x86DD,
 	'Ethernet_Flow_Control':0x8808,
 	'Ethernet_Slow_Protocols':0x8809,
	'CobraNet':0x8819,
 	'MPLS_Unicast':0x8847,
	'MPLS_Multicast':0x8848,
	'PPPoE_Discovery_Stage':0x8863,
	'PPPoE_Session_Stage':0x8864,
	'Intel_Advanced_Networking_Services':0x886D,
	'Jumbo_Frames':0x8870,
 	'HomePlug':0x887B,
 	'EAP_over_LAN':0x888E,
 	'PROFINET_Protocol':0x8892,
 	'HyperSCSI':0x889A,
	'ATA_over_Ethernet':0x88A2, 
	'EtherCAT':0x88A4,
 	'Provider_Bridging':0x88A8,
 	'Ethernet_Powerlink':0x88AB,
	'GOOSE':0x88B8,
	'GSE':0x88B9, 
 	'SV':0x88BA,
	'LLDP':0x88CC, 
	'SERCOS':0x88CD, 
	'WSMP':0x88DC, 
	'HomePlug':0x88E1,
	'Media_Redundancy':0x88E3,
	'MAC_Security':0x88E5,
	'PBB':0x88E7,
	'PTP':0x88F7,
	'NC-SI':0x88F8,
	'PRP':0x88FB,
	'CFM':0x8902,
 	'FCoE':0x8906,
 	'FCoE_Initialization':0x8914,
 	'RoCE':0x8915,
 	'TTE':0x891D,
 	'HSR':0x892F,
 	'Ethernet_Testing_Protocol':0x9000,
 	'VLAN_double_tagging':0x9100

}


class Ethernet():
	def __init__(self):
		self.src_mac = ''
		self.dst_mac = ''
		self.type = 0x0800 # ip V4  testing sin capa superior
		#self.type = 0x9000
		self.data = ''

	def create(self):
		return pack("!6s6sH",unhexlify(self.dst_mac.replace(":","")),unhexlify(self.src_mac.replace(":","")),self.type)

class EthernetARP(Ethernet):
	def __init__(self):
		Ethernet.__init__(self)
		
	def create(self):
		self.type = 0x0806
		return Ethernet.create(self)