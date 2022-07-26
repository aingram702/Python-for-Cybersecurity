from scapy.all import *
import ipaddress

ports = [20,21,22,23,25,53,67,68,69,80,110,119,123,135,136,137,138,139,143,156,161,162,179,194,389,443,445,8080,8443]

def SynScan(host):
    ans,unans = sr(
        IP(dst=host)/
        TCP(sport=33333,dport=ports,flags="S")
        ,timeout=2,verbose=0)
    print("-------------------------------------Open ports at %s:-----------------------------------" % host)
    for (s,r,) in ans:
        if s[TCP].dport == r[TCP].sport and r[TCP].flags=="SA":
            if (s[TCP].dport == 20):
                print(s[TCP].dport, " is -----OPEN-----")
                print("Service running on 20 is FTP: File Transfer Protocol")
            if (s[TCP].dport == 21):
                print(s[TCP].dport, " is -----OPEN-----")
                print("Service running on 21 is FTP: File Transfer Protocol")
            if (s[TCP].dport == 22):
                print(s[TCP].dport, " is -----OPEN-----")
                print("Service running on 22 is SSH: Secure Shell Protocol")
            if (s[TCP].dport == 23):
                print(s[TCP].dport, " is -----OPEN-----")
                print("Service running on 23 is Telnet: The Insecure Shell Protocol")
            if (s[TCP].dport == 25):
                print(s[TCP].dport, " is -----OPEN-----")
                print("Service running on 25 is SMTP: Simple Mail Transfer Protocol")
            if (s[TCP].dport == 53):
                print(s[TCP].dport, " is -----OPEN-----")
                print("Service running on 53 is DNS: Domain Name System Protocol")
            if (s[TCP].dport == 67):
                print(s[TCP].dport, " is -----OPEN-----")
                print("Service running on 67 is DHCP: Dynamic Host Configuration Protocol")
            if (s[TCP].dport == 68):
                print(s[TCP].dport, " is -----OPEN-----")
                print("Service running on 68 is DHCP: Dynamic Host Configuration Protocol")
            if (s[TCP].dport == 69):
                print(s[TCP].dport, " is -----OPEN-----")
                print("Service running on 69 is TFTP: Trivial File Transfer Protocol")
            if (s[TCP].dport == 80):
                print(s[TCP].dport, " is -----OPEN-----")
                print("Service running on 80 is HTTP: Hypertext Transfer Protocol")
            if (s[TCP].dport == 110):
                print(s[TCP].dport, " is -----OPEN-----")
                print("Service running on 110 is POP3: Post Office Protocol Version 3")
            if (s[TCP].dport == 119):
                print(s[TCP].dport, " is -----OPEN-----")
                print("Service running on 119 is NNTP: Network News Transfer Protocol")
            if (s[TCP].dport == 123):
                print(s[TCP].dport, " is -----OPEN-----")
                print("Service running on 123 is NTP: Network Time Protocol")
            if (s[TCP].dport == 135):
                print(s[TCP].dport, " is -----OPEN-----")
                print("Service running on 135 is RPC NETBIOS: Remote Procedure Call Protocol")
            if (s[TCP].dport == 136):
                print(s[TCP].dport, " is -----OPEN-----")
                print("Service running on 136 is PNS NETBIOS: Profile Naming System Protocol")
            if (s[TCP].dport == 137):
                print(s[TCP].dport, " is -----OPEN-----")
                print("Service running on 137 is NETBIOS: NETBIOS Name Service Protocol")
            if (s[TCP].dport == 138):
                print(s[TCP].dport, " is -----OPEN-----")
                print("Service running on 138 is NETBIOS: NETBIOS Datagram Service Protocol")
            if (s[TCP].dport == 139):
                print(s[TCP].dport, " is -----OPEN-----")
                print("Service running on 139 is NETBIOS: NETBIOS Session Service Protocol")
            if (s[TCP].dport == 143):
                print(s[TCP].dport, " is -----OPEN-----")
                print("Service running on 143 is IMAP4: Internet Message Access Protocol Version 4")
            if (s[TCP].dport == 156):
                print(s[TCP].dport, " is -----OPEN-----")
                print("Service running on 156 is SQL: Structured Query Language Service Protocol")
            if (s[TCP].dport == 161):
                print(s[TCP].dport, " is -----OPEN-----")
                print("Service running on 161 is SNMP: Simple Network Management Protocol")
            if (s[TCP].dport == 179):
                print(s[TCP].dport, " is -----OPEN-----")
                print("Service running on 179 is BGP: Border Gateway Protocol")
            if (s[TCP].dport == 194):
                print(s[TCP].dport, " is -----OPEN-----")
                print("Service running on 194 is IRC: Internet Relay Chat Protocol")
            if (s[TCP].dport == 389):
                print(s[TCP].dport, " is -----OPEN-----")
                print("Service running on 389 is LDAP: Lightweight Directory Access Protocol")
            if (s[TCP].dport == 443):
                print(s[TCP].dport, " is -----OPEN-----")
                print("Service running on 443 is HTTPS: HTTP Secure Protocol")      
            if (s[TCP].dport == 445):
                print(s[TCP].dport, " is -----OPEN-----")
                print("Service running on 445 is SMB: Server Message Block Protocol")
            if (s[TCP].dport == 8080):
                print(s[TCP].dport, " is -----OPEN-----")
                print("Service running on 8080 is for proxying and caching.")
                print("This port is commonly used for reverse shells, remote access, and other ")
                print("malicious purposes. !!!!Monitor this port very closely!!!!")
            if (s[TCP].dport == 8443):
                print(s[TCP].dport, " is -----OPEN-----")
                print("Service running on 8443 is a common HTTPS port.")
                print("This port is commonly used for web applications using SSL.")
                print("Web Services like Apache run on this port. Also some IOT and")
                print("networking equipment like Ubiquiti UniFi also use the port.")                 
        elif s[TCP].dport == r[TCP].sport and r[TCP].flags == "R":
            print(s[TCP].dport, " is closed")
        else:
            print(s[TCP].dport, " is filtered by a firewall")


def DNSScan(host):
    ans,unans = sr(
        IP(dst=host)/
        UDP(dport=53)/
        DNS(rd=1,qd=DNSQR(qname="google.com"))
        ,timeout=2,verbose=0)
    if ans and ans[UDP]:
        print("DNS Server at %s"%host)




host = input("Enter Target IP Address: ")
try:
    ipaddress.ip_address(host)
except:
    print("Invalid IP Address. Double-check and try again....")
    exit(-1)


SynScan(host)
DNSScan(host)