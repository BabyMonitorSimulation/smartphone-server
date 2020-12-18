from project import app
from flask import request, jsonify
from project.communication.client_smp import ClientSMP
import threading
from time import sleep


client_smp = ClientSMP()
client_smp.subscribe()
confirmation = False

def wait_for_confirmation(self):
    global confirmation, client_smp

    time = 0
    while not confirmation:
        print(f"I'm waiting for {time} seconds.")
        if time >= 7:
            client_smp.publish_to_smp(confirmation)
            break
        sleep(1)
        time += 1

@app.route("/", methods=["GET"])
def check():
    return "I'm working Smartphone"


@app.route("/smp_receive_confirmation", methods=["GET"])
def smp_receive_confirmation():
    global client_smp, confirmation
    
    confirmation = True
    client_smp.publish_to_smp(confirmation)

    return "OK"


@app.route("/smp_receive_notification", methods=["GET"])
def smp_receive_notification():
    global client_smp
    
    threading.Thread(target=wait_for_confirmation).start()
    
    return "OK"
