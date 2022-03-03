#!/usr/bin/sudo python3

from scapy.all import *
from scapy.layers.inet import UDP, IP
from scapy.layers.l2 import Ether


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

def craftingAndSendingPacket():
    pkt = Ether()/IP()/UDP()/"data"
    send (pkt)
    
def createPingPacketAndTrackResponse():
    packet = IP(dst="www.google.com")/ICMP()/"Hello there!"
    recivedData = sr1(packet) # sr1 = send and recive
    recivedData.show()

def SendingLotsOfPacketsForCreatingDosAttack():
    send(IP(src="192.168.1.103",dst="192.168.1.1")/TCP(sport=80,dport=80),count=100)

def readPcap():
    ''' in order to create this pecap ive opened wireshark and recorded hten i
    have stopped the record and saved a pcap file with the info
    that were recorded untill the stoppin '''
    p = rdpcap("/home/itsik/scapyPcaps/youtube.pcap")
    print(p)
    print("number of packets: " ,len(p)) # How many packets
    singelPacketFromAllPecap = p[5] # getting the 1000th packet within our pecap
    print("\n single packet: " ,singelPacketFromAllPecap)
    print ("\nThe type of the singel packet: " , type(singelPacketFromAllPecap))
    print("\n Hex presentation of the packet: ", hexdump(singelPacketFromAllPecap))
    print("\n all packet fileds: \n" , displayAllPacketFields(singelPacketFromAllPecap))
    print("Show all the packet layers and info: \n")
    singelPacketFromAllPecap.show()
def getListOfScapyFunctions():
    print(lsc())

def displayAllPacketFields(pkt):
    ''' source port, dst port, for example if the src port is 443 , the packet came from
    an https server'''
    ls(pkt)


craftingAndSendingPacket()
# getListOfScapyFunctions()
# readPcap()
# SendingLotsOfPacketsForCreatingDosAttack()
#sniffingPakcetsFromSpesificProtocol()
# createPingPacket()
# createPingPacketAndTrackResponse()
