#coding:utf-8
import paho.mqtt.client as mqtt
from bridge import WebsocketBridge

class MQTTClient(WebsocketBridge):
    def __init__(self, host, port, user, passwd, topic):
        self.topic = topic
        self.client = mqtt.Client()
        self.client.username_pw_set(user, passwd) # 必须设置，否则会返回「Connected with result code 4」
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(host, port, 60)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        # print("Connected with result code "+str(rc))
        self.client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        print msg.topic+" "+str(msg.payload)
        # print userdata
        self.broadcast(msg.payload)

