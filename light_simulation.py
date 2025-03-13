import paho.mqtt.client as mqtt

broker = "test.mosquitto.org"
topic = "/student_group/light_control"

def on_message(client, userdata, message):
    command = message.payload.decode()
    if command == "ON":
        print("💡 Light is TURNED ON")
    elif command == "OFF":
        print("💡 Light is TURNED OFF")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)  # Use the latest API version
client.on_message = on_message
client.connect(broker, 1883, 60)

client.subscribe(topic)
client.loop_forever()
