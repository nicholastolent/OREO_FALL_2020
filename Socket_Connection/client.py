import socket
import configparser as CP
import os

configParser = CP.RawConfigParser()
configFilePath = 'config.conf'
configParser.read(configFilePath)

HOST = configParser.get('Host.IP.Info', 'ADDRESS')
PORT = int(configParser.get('Host.IP.Info', 'PORT'))

fileName = "testMsg.txt"

filesize = os.path.getsize(fileName)

message = "Hello World"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as s:
    s.connect((HOST,PORT))
    s.send(message.encode('utf8'))
    data = s.recv(1024)
    
print('Received', repr(data.decode()))