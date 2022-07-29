import ftplib, telnetlib
from time import sleep


def FTPConnection(ip, username, password):
    ftp = ftplib.FTP(host=ip,user=username,passwd=password)
    sleep(5)
    ftp.quit()
    
def TelnetConnection(ip, username, password):
    telnet = telnetlib.Telnet(ip)
    telnet.read_until(b"login: ")
    telnet.write(bytes(username+"\n","utf-8"))
    telnet.read_until(b"Password: ")
    telnet.write(bytes(password+"\n","utf-8"))
    telnet.read_all()
    sleep(1)
    telnet.write(b"exit\n")
    
    
    
ip = "3.20.135.129"
username = "fake"
password = "fake"
TelnetConnection(ip,username,password)