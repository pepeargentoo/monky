from  attack.lan import Lan
#from time import time

print "inicio test"
mac = Lan()
mac.MacOverflow('wlan0')
print " fin test"