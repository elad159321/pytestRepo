#!/usr/bin/sudo python3

from scapy.all import *

def sniffingAndPrintingRandomPackets():
    resuls = sniff(count=10)
    print (resuls[3].show())

def sniffingPakcetsFromSpesificProtocol():
    results = sniff(count=10, filter="icmp")
    print (results.show())
# sniffingAndPrintingRandomPackets()

def createPingPacket():
    packet = Ether()/IP(dst="www.google.com")/ICMP()/"hello!"
    sendp(packet)

def createPingPacketAndTrackResponse():
    packet = IP(dst="www.google.com")/ICMP()/"Hello there!"
    recivedData = sr1(packet) # sr1 = send and recive
    recivedData.show()

def SendingLotsOfPacketsForCreatingDosAttack():
    send(IP(src="192.168.1.103",dst="192.168.1.1")/TCP(sport=80,dport=80),count=100)

# SendingLotsOfPacketsForCreatingDosAttack()
#sniffingPakcetsFromSpesificProtocol()
createPingPacket()
# createPingPacketAndTrackResponse()
