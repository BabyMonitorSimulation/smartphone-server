from project import app
from flask import request, jsonify
from pŕoject.services.smartphone_service import last_record, insert_data
from project.communication.client_smp import ClientSMP
import threading
from time import sleep


client_smp = ClientSMP()
confirmation = False # confirmation from user
call_once = True # wait for confiramtion one single time if smp receive a notification


def back_to_init_configuration():
    return False, True


def wait_for_confirmation(self):
    global confirmation, client_smp

    time = 0
    while not confirmation:
        print(f"I'm waiting for {time} seconds.")
        if time >= 7:
            notification = last_record()
            client_smp.publish_to_smp(notification)
            break
        sleep(1)
        time += 1

@app.route("/", methods=["GET"])
def check():
    return "I'm working Smartphone"


@app.route("/receive-data", methods=["GET"])
def receive_data():
    global client_smp, confirmation, call_once

    baby_data = {
        "breathing": request.json["breathing"],
        "time_no_breathing": request.json["time_no_breathing"],
        "crying": request.json["crying"],
        "sleeping": request.json["sleeping"],
    }

    inser_data(baby_data)

    if request.json["type"] == "notification" and call_once:
        call_once = False
        threading.Thread(target=wait_for_confirmation).start().join()

    return "OK"


@app.route("/confirmation", methods=["GET"])
def confirmation():
    global client_smp, confirmation, call_once

    confirmation = True
    client_smp.publish_to_bm()
    sleep(1) # wait a time to smp back to init configuration
    confirmation, call_once = back_to_init_configuration()
    
    return "OK"

