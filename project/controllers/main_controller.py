from project import app
from flask import request, jsonify
from project.services.smartphone_service import last_record, insert_data
from project.communication.client_smp import ClientSMP
import threading
from time import sleep


client_smp = ClientSMP()
confirmation = False  # confirmation from user
call_once = True  # wait for confiramtion one single time if smp receive a notification


def back_to_init_configuration():
    return False, True


def wait_for_confirmation():
    global confirmation, client_smp

    time = 0
    while not confirmation:
        print(f"I'm waiting for {time} seconds.")
        if time >= 7:
            notification = last_record()
            client_smp.publish_to_dojot(notification)
            break
        sleep(1)
        time += 1


@app.route("/", methods=["GET"])
def check():
    return "I'm working Smartphone"


@app.route("/receive-data", methods=["POST"])
def receive_data():
    global client_smp, confirmation, call_once
    print(f"received: {request.json}")
    if request.json["from"] == "bm":
        baby_data = {
            "breathing": request.json["breathing"],
            "time_no_breathing": request.json["time_no_breathing"],
            "crying": request.json["crying"],
            "sleeping": request.json["sleeping"],
        }
        insert_data(baby_data)

        if request.json["type"] == "notification" and call_once:
            call_once = False
            threading.Thread(target=wait_for_confirmation).start()

    elif request.json["from"] == "tv":
        if request.json["msg"] == "unlocked":
            call_once = True
            confirmation = False
            data = {
                "msg": "Confirmation Received",
                "from": "smp",
                "to": "bm",
                "type": "confirmation",
            }
            client_smp.publish_to_bm(data)

    return "OK"


@app.route("/get_confirmation", methods=["GET"])
def get_confirmation():
    global client_smp, confirmation, call_once
    call_once = True
    confirmation = True
    data = {
        "msg": "Confirmation Received",
        "from": "smp",
        "to": "bm",
        "type": "confirmation",
    }
    client_smp.publish_to_bm(data)
    sleep(1)  # wait a time to smp back to init configuration
    confirmation, call_once = back_to_init_configuration()

    return "OK"

