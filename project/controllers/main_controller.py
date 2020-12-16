from project import app, client_smp
from flask import request, render_template, send_from_directory, jsonify, send_file
from project.util.response import construct_response
from project.services.smartphone_service import insert_data, last_record
from time import sleep
from pprint import pprint
import json
import requests
import threading
import paho.mqtt.client as mqtt


@app.route("/check", methods=["GET"])
def check():
    return "I'm working (Smartphone)"


@app.route("/smp_send", methods=["GET"])
def send_bm():
    client_smp.confirmation = True

    body = {
        "type": "confirmation",
        "msg": "The notification is confirmed",
        "from": "smp",
        "to": "bm",
    }
    client_smp.publish_to_bm(body)

    return "OK"
