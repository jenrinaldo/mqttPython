import paho.mqtt.client as mqtt
import time

ip = "127.0.0.1"
topikPub = "/status/1"
topikSub = "/beli/1"
port = 1883
saldo = 100000
bankPayload = ""

client = mqtt.Client(client_id="pubSub2",clean_session=False)

def on_message(client, obj, msg):
    pulsa = int(msg.payload.decode("utf-8"))
    global saldo
    if pulsa <= saldo and saldo!=0:
        saldo -= pulsa
        bankPayload = str(saldo) + " sukses"
    else :
        bankPayload = "gagal"
    print("Publish to ",topikPub)
    print(bankPayload)
    client.publish(topikPub, payload=bankPayload, qos=2)

client.on_message = on_message
print("Connect to ",ip)
client.connect(ip, port=port)
print("Subscribe to",topikSub)
client.subscribe(topikSub, qos=2)
client.loop_forever()
