import socket
import json
import datetime


HOST = '192.168.0.103'
PORT = 80
BUFFER_SZ = 4096

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as skt:
    skt.connect((HOST, PORT))
    skt.sendall(b"GET / HTTP/1.1\r\n\r\n")
    data = skt.recv(BUFFER_SZ)

reading = {}
json_response = json.loads(data)
reading[datetime.datetime.now().isoformat()] = json_response

with open('esp_moist.log', mode='a', encoding='utf-8') as f:
    json.dump(str(reading)+'\n', f)
