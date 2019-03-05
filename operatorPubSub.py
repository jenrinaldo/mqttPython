import paho.mqtt.client as mqtt
import datetime

ip = "127.0.0.1"
port = 1883
topikSub = "/status/1"
topikPub = "/keClient/1"
operatorPayload = ""
client = mqtt.Client(client_id="pubSub3",clean_session=False)


def on_message(client, obj, msg):
    currentDT = datetime.datetime.now()
    currentDT = currentDT.strftime("%Y-%m-%d %H:%M:%S")
    currentDT = str(currentDT)
    status = msg.payload.decode("utf-8").split(' ')
    if len(status)>1 and status[1] == "sukses":
        strTotal = currentDT+" "+status[0]+ " sukses"
        operatorPayload = str(strTotal)
    else:
        operatorPayload = status[0]
    print("Publish to ",topikPub)
    print(operatorPayload)
    client.publish(topikPub, payload=operatorPayload, qos=2)
client.on_message = on_message
print("Connect to ",ip)
client.connect(ip, port=port)
print("Subscribe to",topikSub)
client.subscribe(topikSub, qos=2)
client.loop_forever()
