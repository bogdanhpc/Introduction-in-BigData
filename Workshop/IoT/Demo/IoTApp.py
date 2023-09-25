from typing import NewType
import paho.mqtt.client as mqtt
import time

# brokerEclipse = "mqtt.eclipseprojects.io"
# brokerHive = "broker.hivemq.com"
# brokerLocalHost = "localhost"
brokerAzure = "20.5.77.27"

def on_log(client,userdata,level,buf):
    print("log: " + buf)

def on_connect(client,userdata, flags,rc):
    if rc==0:
        print("Connected OK!")
        client.subscribe("BigData/IoT/chat/#")
    else:
        print("Connection error!",rc)

def on_disconnect(client,userdata,flags,rc=0):
    print("Disconnected with status code:" + str(rc))

def on_message(client,userdata,msg):
    topic = msg.topic
    decodedMessage = str(msg.payload.decode("utf-8"))
    print("Topic: " + topic + "Message received: " + decodedMessage)


client = mqtt.Client("ClientBogdan2") # creaza un client cu ID-ul Test

#client.on_log = on_log
client.on_disconnect = on_disconnect
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(brokerAzure, 1883, 60)


client.loop_start()

while 1:
    msg = input("Mesaj: ")
    client.publish("BigData/IoT/chat/Bogdan2", str(msg))
    time.sleep(2)
