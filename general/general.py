from random import randint,choice
from socket import socket,AF_INET,SOCK_DGRAM,inet_aton,SOCK_STREAM
from struct import pack
from fcntl import ioctl

class General():
	def get_mac(self,ifname):
		s = socket(AF_INET, SOCK_DGRAM)
		info = ioctl(s.fileno(), 0x8927, pack('256s', ifname[:15]))
		return ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]

	def mac_random(self):
		mac = ''
		for i in range(5):
			mac+=self.sub_mac()+':'
		mac+=self.sub_mac()
		return mac

	def sub_mac(self):
		hexa = '0123456789abcdef'
		return choice(hexa)+choice(hexa)

	def set_mac(self,iface,mac=False):
		SIOCGIFHWADDR = 0x8927 
		resp = {'mac_old':'','mac_new':''}
		sock = socket(AF_INET, SOCK_DGRAM,0)

		resp['mac_old'] = self.get_mac(iface)
		if mac == False:
			mac = self.mac_random()	
		resp['mac_new'] = mac
		mac = inet_aton(mac)
		ifreq = pack('16sH2s4s8s',iface,AF_INET,'\x00'*2,mac,'\x00'*8)
		print(ifreq)
		ioctl(sock, SIOCGIFHWADDR, ifreq)
		#ioctl(net->sock, SIOCSIFHWADDR, &net->dev)
		#print(iface,mac,resp)

	def get_ip(self):
		ip = socket(AF_INET,SOCK_DGRAM)
		ip.connect(("8.8.8.8",80))
		return ip.getsockname()[0]

	def ip_random(self):
		return str(randint(0,255))+'.'+str(randint(0,255))+'.'+str(randint(0,255))+'.'+str(randint(0,255))

	def set_ip(self,iface,ip=False):
		if ip == False:
			ip = self.ip_random()
		SIOCSIFADDR = 0x8916
		sock = socket(AF_INET, SOCK_STREAM)
		ip = inet_aton(ip)
		ifreq = pack('16sH2s4s8s',iface,AF_INET,'\x00'*2,ip,'\x00'*8)
		ioctl(sock, SIOCSIFADDR, ifreq)
	

