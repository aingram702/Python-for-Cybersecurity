import socket
from Crypto.Cipher import AES

host = "127.0.0.1" # can be any IP you like, but compatible with Client
port = 1337

key = b"Sixteen byte key"


def decrypt(data,key,iv):
    cipher = AES.new(key,AES.MODE_CBC,iv)
    return cipher.decrypt(data)

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((host,port))
    s.listen()
    conn.addr = s.accept()
    with conn:
        iv = conn.recv(16)
        length = conn.recv(1)   # assumes short messages.
        data = conn.recv(1024)
        while True:
            d = conn.recv(1024)
            if not d:
                break
            data += d
        plaintext = decrypt(data,key,iv).decode("utf-8")[:ord(length)]
        print("Received: %s"% plaintext) 
