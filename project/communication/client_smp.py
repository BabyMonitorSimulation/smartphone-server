from project.services.smartphone_service import insert_data
import threading
import paho.mqtt.client as mqtt
from time import sleep
import json


class ClientSMP:
    def __init__(self):
        self.client = mqtt.Client("smp")
        self.client.connect(host="dojot.atlantico.com.br", port=1883)
        self.confirmation = False

    #send to smp in dojot
    def publish_to_smp(self, confirmation):
        data = {'msg': 'Confirmation Received' if confirmation else 'Confirmation not Received'}
        self.client.publish("/gesad/434339/attrs", payload=json.dumps(data))

