# DataClient2.py

from tcpcom import TCPClient, ClientHandler
import time


IP_ADDRESS = "192.168.0.105"
IP_PORT = 80

def onStateChanged(state, msg):
    global isConnected
    if state == "CONNECTING":
       print "Client:-- Waiting for connection..."
    elif state == "CONNECTED":
       print "Client:-- Connection established."
    elif state == "DISCONNECTED":
       print "Client:-- Connection lost."
       isConnected = False
    elif state == "MESSAGE":
       print "Client:-- Received data:", msg

client = TCPClient(IP_ADDRESS, IP_PORT, stateChanged = onStateChanged)
rc = client.connect()
clientHandler = ClientHandler(client)
if rc:
    isConnected = True
    i = 0
    while i < 5: # isConnected:
        print "Client:-- Sending command: go..."
        client.sendMessage("go")
        response = clientHandler.readResponse()
        print(response)
        time.sleep(2)
        i += 1
    print "Done"
    client.disconnect()
else:
    print "Client:-- Connection failed"
