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

# sniffingPakcetsFromSpesificProtocol()

createPingPacket()