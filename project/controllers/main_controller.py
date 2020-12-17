from project import app
from flask import request, jsonify
from project.communication.client_smp import ClientSMP


client_smp = ClientSMP()
client_smp.subscribe()


@app.route("/check", methods=["GET"])
def check():
    return "I'm working (Smartphone)"


@app.route("/smp_send", methods=["GET"])
def send_bm():
    global client_smp
    
    client_smp.confirmation = True

    body = {
        "type": "confirmation",
        "msg": "The notification is confirmed",
        "from": "smp",
        "to": "bm",
    }
    client_smp.publish_to_bm(body)

    return "OK"
