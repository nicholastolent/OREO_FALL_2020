import socket
import configparser as CP

configParser = CP.RawConfigParser()
configFilePath = 'config.conf'
configParser.read(configFilePath)

HOST = configParser.get('Host.IP.Info', 'ADDRESS')
PORT = int(configParser.get('Host.IP.Info', 'PORT'))

endData = False
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn: 
        print('Connected by', addr)
        while not endData:
            try:
                data = conn.recv(1024)     
                if not data:
                    break
                conn.sendall(data)
            except socket.error:
                if socket.errno != errno.EWOULDBLOCK:
                    print('Error: %r' %e)
                    run_main_loop = false
                endData = True
            print(data)
            
