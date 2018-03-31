import socket
import json


HOST = '192.168.0.103'
PORT = 80
BUFFER_SZ = 4096

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as skt:
    skt.connect((HOST, PORT))
    skt.sendall(b"GET / HTTP/1.1\r\n\r\n")
    data = str(skt.recv(BUFFER_SZ))

print('Received', repr(data))

with open('esp_moist.log', mode='w', encoding='utf-8') as f:
    json.dump(data, f)
