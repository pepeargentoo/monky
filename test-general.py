from general.general import General

#inicio test mac_random
a = General()
print(a.mac_random())
#fin test mac_random

#incio ip_random
print(a.ip_random())
#fin ip_random	

#incio get_ip
#print(a.get_ip())
#end get_ip

"""
incio set_ip
print(a.set_ip('wlan0')) #random ip
print(a.set_ip('wlan0','192.168.1.67')) #sobrecarga ip setiado
end set_ip
"""
print(a.set_mac('wlan0'))
