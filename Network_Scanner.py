from scapy.all import *


#Please enter the IP address range you want to scan

ip_range = input("Enter the IP address range you want to scan(example: 192.168.1.0/24): ")

#Function for grabbing Ip address

def scan_network(ip_range):
    packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_range)
    answered = srp(packet, timeout=2, verbose=False)[0]

    for sent, received in answered:
        print ("Device found: {received.psrc} - {received.hwsrc}")

#Runs the Scanner

scan_network(ip_range)
