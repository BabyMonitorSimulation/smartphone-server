from project.services.smartphone_service import insert_data
import paho.mqtt.client as mqtt
from time import sleep
import threading
import json


class ClientSMP:
    def __init__(self):
        self.client = mqtt.Client("smp")
        self.client.connect(host="dojot.atlantico.com.br", port=1883)
        self.confirmation = False

    #send to smp in dojot
    def publish_to_smp(self, notification):
        self.client.publish("/gesad/434339/attrs", payload=json.dumps(notification))

    #send to bm in dojot
    def publish_to_bm(self):
        data = {'msg': 'Confirmation Received'}
        self.client.publish("/gesad/434339/attrs", payload=json.dumps(data))
