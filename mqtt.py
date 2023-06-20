print("MQTT with Adafruit IO")
import time
import random
import sys
from Adafruit_IO import MQTTClient

AIO_FEED_ID = "button1"
AIO_USERNAME = "hejmanh"
AIO_KEY = "aio_lZrz09oRS0P0iGYyzTpu44DWfqcN"

def connected(client):
    print("Server connected ...")
    client.subscribe("button1")
    client.subscribe("button2")

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe!! ...")

def disconnected(client):
    print("Disconnect from server ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Received: " + payload)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:
    time.sleep(5)
    client.publish("sensor1",random.randint(20,70))
    client.publish("sensor2", random.randint(0,100))
    client.publish("sensor3", random.randint(0,1000))
    pass
