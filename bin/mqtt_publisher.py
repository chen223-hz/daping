#coding:utf-8
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import random
import json
import time

HOST = "hiyou.doublecom.net"
PORT = 1883
AUTH = {'username': "admin", 'password':"password"}
TOPIC = 'daping'

#notify = lambda data: publish.single(TOPIC, json.dumps(data), hostname=HOST, port=PORT, auth=AUTH)
mqttc = mqtt.Client("daping_pub")
mqttc.connect(HOST, PORT)
notify = lambda data: mqttc.publish(TOPIC, json.dumps(data))

def random_mac():
    Maclist = []
    for _ in range(1, 7):
        RANDSTR = "".join(random.sample("0123456789ABCDEF",2))
        Maclist.append(RANDSTR)
    return ":".join(Maclist)

if __name__ == '__main__':
    realtime = 3230
    total = 51000
    portal_today = 300
    portal_total = 30000
    print 'working'
    while True:
        notify({
            'action': 'pushRecentUser', 
            'data': {'title': random_mac()}
        })
        realtime += random.randint(-3, 3)
        total += random.randint(0, 2)
        portal_today += random.randint(0, 2)
        portal_total += random.randint(0, 2)
        notify({
            'action': 'setUserCount', 
            'data': {
                'realtime': realtime,
                'total': total,
                'portal_today': portal_today,
                'portal_total': portal_total,
            }
        })
        notify({
            'action': 'updateEnvironment',
            'data': {
                'temp': random.randint(10,20),
                'humidity': random.randint(50, 70),
                'moisture': random.randint(40,80),
                'winds': random.randint(1, 5),
            }
        })
        time.sleep(1.0)
