import socket
HOST = '169.254.175.217'
PORT = 10000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as s:
    s.connect((HOST,PORT))
    s.sendall(b'Hello, World')
    data = s.recv(1024)
    
print('Received', repr(data))