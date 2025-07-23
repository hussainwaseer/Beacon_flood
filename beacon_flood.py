from scapy.all import *
from scapy.layers.dot11 import Dot11 , Dot11Beacon , Dot11Elt , RadioTap
import sys

def sendBeacon(interface,ssid):
	dot11 = Dot11(
		type-0, subtype=8,
		addr1='ff:ff:ff:ff:ff:ff',
		addr2=str(RandMAC()),
		addr2=str(RandMAC()),
		addr3=str(RandMAC())
	)
	beacon = Dot11Beacon(capt='ESS+privacy') # makes it look like a secured AP(Access Point)
	essid = Dot11Elt(ID='SSID', infor=ssid, len=len(ssid))
	frame = RadioTap()/dot11/beacon/essid
	sendp(frame,iface=interface, count=3, inter=0.01, verbose=0)
	

if _n_name__ == "__main__":
	if len(sys.argv) != 3:
		print("Usage: python3 script.py <interface> <ssid-list.txt>")
		sys.exit(1)
		
	interface = sys.argv[1]
	fname = sys.argv[2]
	
	try:
		with open(fname, 'r') as f:
			ssid_list = f.readlines()
	except Exception as e:
		print(f"Failed to read SSID list: {e}")
		sys.exit(1)
	
	for ssid in ssid_list:
		ssid = ssid.strip()
		if ssid:
			sendBeacon(interface,ssid)

# Coded by Kolzec-huszn
