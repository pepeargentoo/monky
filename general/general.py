from random import randint,choice
from socket import socket,AF_INET,SOCK_DGRAM
from struct import pack
from fcntl import ioctl


class General():
	def mac_random(self):
		mac = ''
		for i in range(5):
			mac+=self.sub_mac()+':'
		mac+=self.sub_mac()
		return mac

	def sub_mac(self):
		hexa = '0123456789ABCDEF'
		return choice(hexa)+choice(hexa)	

	def ip_random(self):
		return str(randint(0,255))+'.'+str(randint(0,255))+'.'+str(randint(0,255))+'.'+str(randint(0,255))

	def get_ip(self):
		ip = socket(AF_INET,SOCK_DGRAM)
		ip.connect(("8.8.8.8",80))
		return ip.getsockname()[0]

	def get_mac(self,ifname):
		s = socket(AF_INET, SOCK_DGRAM)
		print(s)
		info = ioctl(s.fileno(), 0x8927, pack('256s', ifname[:15]))
		return ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]