from project import app
from flask import request, render_template, send_from_directory, jsonify, send_file
from project.util.response import construct_response
from project.services.smartphone_service import insert_data, last_record
from time import sleep
from pprint import pprint
import json
import requests
import threading

confirmation = False


def make_request(data):
    requests.post("http://localhost:5003/smp_receive", json=data)


def wait_for_confirmation():
    global confirmation
    time = 0
    while not confirmation:
        print(f"I'm waiting for {time} seconds.")
        if time >= 7:
            data = last_record()
            body = construct_response('notification', data, 'tv')        
            make_request(body)
            break
        sleep(1)
        time += 1


@app.route("/check", methods=["GET"])
def check():
    return "I'm working (Smartphone)"


@app.route("/smp_receive", methods=["POST"])
def receive_bm():
    global confirmation
    body = request.json
    pprint(body)
    if body["route"]["from"] == "bm":
        insert_data(body['msg'])
        if body["type"] == "notification":
            print('Received Notification')
            confirmation = False
            threading.Thread(target=wait_for_confirmation).start()
            return (
                jsonify(construct_response("ack", {"info": "OK"}, "bm")),
                200,
            )

        if body["type"] == "status":
            return (
                jsonify(construct_response("ack", {"info": "OK"}, "bm")),
                200,
            )

    if body["route"]["from"] == "tv":
        # "Tv's blocked"
        if "unlocked" in body['msg']["info"]:
            confirmation = True
            body = {
                "type": "confirmation",
                "msg": {"info": "The notification is confirmed"},
                "route": {"from": "smp", "to": "bm"},
            }
            requests.post("http://localhost:5003/smp_receive", json=body)
            pprint(body['msg']["info"])

        return (
            jsonify(construct_response("ack", {"info": "OK"}, "tv")),
            200,
        )

    return "Error", 400


@app.route("/smp_send", methods=["POST"])
def send_bm():
    body = {
        "type": "confirmation",
        "msg": "The notification is confirmed",
        "route": {"from": "smp", "to": "bm"},
    }
    requests.post("http://localhost:5003/smp_receive", json=body)
