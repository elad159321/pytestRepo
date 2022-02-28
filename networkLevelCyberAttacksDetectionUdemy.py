# Lesson 2 - introduction to scapy
# sneding a packet and view the payload in wireshark

#The most important part of creating costume roles to detect attacks is the payload
#keword are used for creating costum rules
import string

from scapy.all import *
from scapy.layers.dns import DNS, DNSQR
from scapy.layers.inet import IP, TCP, UDP, ICMP
import urllib
import smtplib
def test_sendPacket():
    payload1 = "elad"
    payload2 = "yes"
    payload3 = "anomalUserAgemt"
    payload4 = "method"
    payload5 = "maliciousdomain"
    junk = "\x41" *23
    nop = "\x90" * 34
    alternate = "\x42" * 11
    dataPayload = junk + payload1 + nop + payload2 + 4 * "C" + payload2 + payload4 + 20 * "D" + payload3 + nop + payload5
    pack = IP(dst='172.16.8.53')/TCP(dport=1337,sport=1025)/dataPayload
    send(pack)
    # sr1(pack)

def test_2_sendDNS():
    ''' The lecture use lemnux which asks for DNS, and then with scapy he simulates DNS resonoses from bad resources (malwaere)'''
    maliciousDomainList = ["password-facebook.local,isp-payment-fake.com"]
    for domain in maliciousDomainList:
        query = IP(dst="172.16.8.53")/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname=domain))
        send(query,verbose=0)

def sendICMPPacket():
    packet = IP(src="172.16.8.50",dst="172.16.8.9")/ICMP()/"Data"
    sr1(packet)

def emulateMalwaereBehavior():
    senders = ["security@localdomain.phishing"]
    recivers = ["jack@morningcatch.ph","eladMorninCatch.ph"]

    for sender in senders:
        messege = '''From: From Person <phishing.localdomain>
        To: To Person <eladMorninCatch.ph
        Subject: SPAM
        Hi this is a spam'''

        # try:
        smtpObj = smtplib.SMTP("malwere.localdomain.phishing")
        for reciver in recivers:
            smtpObj.sendmail(sender,reciver,messege)
            print("mail was sent")
        # except:
        #     print("Erronr maill wasnt sent")
        
        
# DNS tabbel attack:

def getRandomString(length):
    domein="c2c-server.local"
    letters = string.ascii_lowercase
    subdom = "".join(random.choice(letters) for i in range(length))
    print("Random string of length" , length, "is:", subdom)
    final = subdom + "." + domein
    queryToDnsServer = IP(dst="172.16.8.106")/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname=final))/"data"
    send(queryToDnsServer)

def sendALotOfDNSReuqests():
    for xx in range(1,20):
        getRandomString(20)

sendALotOfDNSReuqests()
# test_2_sendDNS()
#
# emulateMalwaereBehavior()
# test_sendPacket()

# sendICMPPacket()