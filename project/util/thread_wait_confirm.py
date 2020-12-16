from time import sleep
from project import client_smp
from project.services.smartphone_service import last_record

def wait_for_confirmation(data):
    time = 0
    while not client_smp.confirmation:
        print(f"I'm waiting for {time} seconds.")
        if time >= 7:
            data = last_record()
            client_smp.publish_to_tv(data)
            break
        sleep(1)
        time += 1
