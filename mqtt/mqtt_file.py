from django.conf import settings
import paho.mqtt.client as mqtt
import  time
import json
import ast
from core.models import  Device, Notfication
from django.utils import timezone


MQTT_BROKER_CONFIG = getattr(settings, "MQTT_BROKER_CONFIG", {
    "HOST": "--------", # some mosquito host
    "PORT": 1883, #port to connections
    "USERNAME": "-----", #will check if needed
    "PASSWORD": "---", #will check if needed
    "KEEPALIVE": 60,  # 1minutos
    "QOS": 1,
    "CLIENT_ID": "python_1",
    "TOPIC": "iferm/ht",
})

# mqtt broker
broker_address = MQTT_BROKER_CONFIG.get("HOST")
broker_port = MQTT_BROKER_CONFIG.get("PORT")
mqtt_username = MQTT_BROKER_CONFIG.get("USERNAME")
mqtt_password = MQTT_BROKER_CONFIG.get("PASSWORD")
KEEPALIVE = MQTT_BROKER_CONFIG.get("KEEPALIVE", 60) # 2 minutos
mqtt_qos = MQTT_BROKER_CONFIG.get("QOS", 1) # QOS True

mqtt_client_id = MQTT_BROKER_CONFIG.get("CLIENT_ID")


SUB_TOPICS = ("/n/#", "/p/#")


client = mqtt.Client(clean_session=True,client_id="some")


# Define event callbacks
#for connection purposes if rc =0 then it is oky else something is wrong
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to %s:%s (RC: %s)" % (client._host, client._port, rc))
    else:
        print("Bad connection", rc)

    print("Session present: " + str(flags['session present']))

    for topic in SUB_TOPICS:
        client.subscribe(topic, 1)


time_sss = timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M:%S')

# globvar = ''

def on_message(client,obj, msg):
    print("checking")
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    data = msg.topic + " " + str(msg.payload.decode("utf-8", "ignore"))
    m_decode = str(msg.payload.decode("utf-8", "ignore"))
    print("Received data", m_decode)
    top = msg.topic

    pass1 ='2812'
    pass2 = '1994'
    pass3= '3223'


    if top.startswith("/p/", 0, 3):
        print("this password")
        sp = top.split("/")
        imei = "".join(sp[2])
        print(imei)

        d = Device.objects.get(imei=imei)
        if d:

            if m_decode ==pass1:
                Notfication.objects.create(device=d,by_who="Sebuhi Shukuorv",notification_type="Nolu cihaz açıldı",time_s=time_sss)
            elif m_decode ==pass2:
                Notfication.objects.create(device=d,by_who="Huseyin Qemberov",notification_type="Nolu cihaz açıldı",time_s=time_sss)
            elif m_decode == pass3:
                Notfication.objects.create(device=d,by_who="Elgiz Ibrahimli",notification_type="Nolu cihaz açıldı",time_s=time_sss)

            else:
                print("ise dusdu")
                Notfication.objects.create(device=d,by_who="Kənar şəxs", notification_type="Nolu cihazı açmağa cəhd göstərildi",
                                           time_s=time_sss)



    elif top.startswith("/n/",0,3):
        sp = top.split("/")
        imei = "".join(sp[2])
        # print(imei)
        # print(m_decode)
        # m_decode = m_decode.split(",")
        print(type(m_decode))
        new= m_decode.split(",")
        print(new)
        lat = float(new[0])
        lon = float(new[1])


        try:

            d= Device.objects.filter(imei=imei).last()
            if d:

                Device.objects.filter(imei=d).update(device_lat=lat,device_long=lon, tempureture=new[2],
                                        humudity=int(new[3]),pressure=new[4], time_s=time_sss)

                print("I am updated ")
            else:
                pass
        except Exception as err:
            print(err)

    else:
        print("so")



def on_log(client, userdata, level, string):
    print(string)

def on_publish(client, obj, mid):
    print("Data pubslished mid" + str(mid))


def on_disconnect(client, userdata, rc):


    if rc != 0:


        print("Unexpected disconnection for some reasons.", rc)
        client.reconnect()
    else:
        print("Disconnected")


def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


#need to assing callbacks
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.on_subscribe = on_subscribe
client.on_disconnect = on_disconnect
client.on_log = on_log


client.username_pw_set(mqtt_username, mqtt_password)
# Connect to MQTT broker
client.connect(broker_address, broker_port, KEEPALIVE)
print("connecting to broker", broker_address)
