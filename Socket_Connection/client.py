import socket
import configparser as CP

configParser = CP.RawConfigParser()
configFilePath = 'config.conf'
configParser.read(configFilePath)

HOST = configParser.get('Host.IP.Info', 'ADDRESS')
PORT = int(configParser.get('Host.IP.Info', 'PORT'))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as s:
    s.connect((HOST,PORT))
    s.sendall(b'Hello, World')
    data = s.recv(1024)
    
print('Received', repr(data))