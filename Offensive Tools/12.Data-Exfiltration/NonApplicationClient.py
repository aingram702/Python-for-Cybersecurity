from scapy.all import *

def transmit(message,host):
    for m in message:
        packet = IP(dst=host)/ICMP(code = ord(m))
        send(packet)

host = ""
message = "Hello World"
transmit(message,host)