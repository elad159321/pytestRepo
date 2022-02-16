from scapy.all import *

def sniffingAndPrintingRandomPackets():
    resuls = sniff(count=10)
    print (resuls.show())


sniffingAndPrintingRandomPackets()