import paho.mqtt.client as mqtt
import json
import time


# mosquitto_pub -h dojot.atlantico.com.br -p 1883  -t /gesad/9e4ed4/attrs -m '{"breathing": true, "crying": true, "from": "bm", "sleeping": true, "time_no_breathing": 0, "to": "smp", "type": "notification" }'


class ClientSMP(mqtt.Client):
    def __init__(self):
        super().__init__("smp")
        self.on_connect = self.on_connect
        self.on_publish = self.on_publish
        self.connect(host="dojot.atlantico.com.br", port=1883)
        self.connected = False

    def publish_to_dojot(self, data):
        data["from"] = "smp"
        data["to"] = "tv"
        data["type"] = "notification"
        self.connect(host="dojot.atlantico.com.br", port=1883)
        self.publish("/gesad/ff3e63/attrs", payload=json.dumps(data), qos=1)
        self.disconnect()

    def publish_to_bm(self, data):
        self.connect(host="dojot.atlantico.com.br", port=1883)
        self.publish("/gesad/829bac/attrs", payload=json.dumps(data), qos=1)
        self.disconnect()

    def on_publish(self, client, userdata, result):
        print('Message published')

    def on_connect(self, client, userdata, flags, rc):
        self.connected = True
        print("Connected with result code " + str(rc))

