from time import sleep
from project.controllers.main_controller import client_smp

def wait_for_confirmation(data):
    time = 0
    while not client_smp.confirmation:
        print(f"I'm waiting for {time} seconds.")
        if time >= 7:
            client_smp.publish_to_tv(data)
            break
        sleep(1)
        time += 1
