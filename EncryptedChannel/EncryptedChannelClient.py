import socket, os
from Crypto.Cipher import AES

host = "127.0.0.1" # edit to whatever IP you would like
port = 1337

key = b"Sixteen byte key"

def encrypt(data,key,iv):
    # Pad data as needed
    data += " "*(16 - len(data) % 16)
    cipher = AES.new(key,AES.MODE_CBC,iv)
    return cipher.encrypt(bytes(data,"utf-8"))

message = "Hello World" # message can be anything you like

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host,port))
    iv = os.urandom(16)
    s.send(iv)
    s.send(bytes([len(message)]))
    encrypted = encrypt(message,key,iv)
    print("Sending %s" % encrypted.hex())
    s.sendall(encrypted)
