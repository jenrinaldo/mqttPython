import paho.mqtt.client as mqtt
import time
ip = "127.0.0.1"
port = 1883
topikSub = "/keClient/1"
topikPub = "/beli/1"
nominal = str(10000)
client = mqtt.Client(client_id="pubSub1",clean_session=False)

def on_message(client, obj, msg):
    print(msg.payload.decode("utf-8"))
    
client.on_message = on_message
print("Connect to ",ip)
client.connect(ip, port=port)
print("Publish to ",topikPub)
client.loop_start()
client.publish(topikPub, payload=nominal, qos=2)
print("Subscribe to ",topikSub)
client.subscribe(topikSub, qos=2)
time.sleep(1)
client.loop_stop()