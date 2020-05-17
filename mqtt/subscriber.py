"""This script is an example of subscriber to CloudMQTT Broker"""

from urllib.parse import urlparse
import os
import paho.mqtt.client as mqtt
import time

# Define event callbacks
def on_connect(mosq, obj, rc):
    print('Reconnect: {}'.format(str(rc)))

def on_message(mosq, obj, msg):
    # message = str(msg.payload)
    print('Topic: {}/{}'.format(msg.topic, msg.payload.decode('utf-8')))

def on_subscribe(mosq, obj, mid, granted_qos):
    print('Subscribed: {}, QoS: {}'.format(str(mid), str(granted_qos)))

def on_log(mosq, obj, level, string):
    print(string)

#username = 'your username'
#password = 'your password'
#host_url = 'your cloud broker url'
#host_port = 'your cloud broker port' # do not type string, but change to integer
broker_address= 'mqtt.eclipse.org'
port =  1883 # do not type string, but change to integer

mqttc = mqtt.Mosquitto()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Uncomment to enable debug messages
#mqttc.on_log = on_log

# Parse CLOUDMQTT_URL (or fallback to localhost)
url_str = os.environ.get('CLOUDMQTT_URL', broker_address)
url = urlparse(url_str)

# Connect
#username = 'your username'
#password = 'your password'
#mqttc.username_pw_set(username, password)
mqttc.connect(broker_address, port)

# Subscribe to a topic
mqttc.subscribe('myhome/+/kitchen', 0)

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = mqttc.loop()
    time.sleep(2)
print('Reconnect: ' + str(rc))