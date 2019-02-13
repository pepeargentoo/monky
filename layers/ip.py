from socket import inet_aton 
from struct import pack


class IP():
	def __init__(self):	
		self.src_ip = ''
		self.dst_ip = ''
		self.ip_ver = 4
		self.ip_ihl = 5
		self.ip_tos = 0
		self.ip_tot_len = 0
		self.ip_tot_len = 0 
		self.ip_frag_off = 0
		self.ip_ttl = 100
		self.ip_id = 54321	
		self.ip_proto = 5
		self.ip_check = 0  

	def create(self):
		self.ip_ihl_ver = (self.ip_ver << 4) + self.ip_ihl
		self.src_ip = inet_aton(self.src_ip)
		self.dst_ip = inet_aton(self.dst_ip)
		return pack('!BBHHHBBH4s4s',self.ip_ihl_ver,self.ip_tos,self.ip_tot_len, self.ip_id, self.ip_frag_off, self.ip_ttl, self.ip_proto, self.ip_check, self.src_ip, self.dst_ip)
	