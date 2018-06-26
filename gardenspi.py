from flask import Flask
import paho.mqtt.client as mqtt
# https://tutorials-raspberrypi.com/raspberry-pi-mqtt-broker-client-wireless-communication/


application = Flask(__name__)
client = mqtt.Client()
MQTT_SERVER = 'localhost'
MQTT_TOPIC = 'topic'

def on_connect(client, userdata, flags, rc):
    print("Connected with result code" + str(rc))
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

client.on_connect = on_connect
client.on_message = on_message

@application.route("/")
def main():
    client.connect(MQTT_SERVER, 1883, 60)
    return client.on_message

if __name__ == "__main__":
    application.run(host='0.0.0.0')
