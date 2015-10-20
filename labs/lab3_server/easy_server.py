# Echo server program
import socket
import time

HOST = '127.0.0.1'        
PORT = 50007              
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('Connected client')
while 1:
    data = conn.recv(1024)
    if not data:
        break
    else:        
        print('Received[2]: ', data)    
    conn.send(data)
    print('Send[3]: ', data)
conn.close()
