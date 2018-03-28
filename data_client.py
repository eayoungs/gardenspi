import socket


HOST = '192.168.0.111'
PORT = 80
BUFFER_SZ = 4096

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as skt:
    skt.connect((HOST, PORT))
    skt.sendall(b"GET / HTTP/1.1\r\n\r\n")
    data = skt.recv(BUFFER_SZ)

print('Received', repr(data))
