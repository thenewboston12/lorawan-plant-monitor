import sensors
import lorawan
import struct
import time

lorawan.connect_lorawan()

# Socket to use for sending data
from lorawan import s

def send_data():
    air_t, light, soil_t = sensors.measure()

    # Print sensor readings
    print("Ambient Light : %.2f lux" % light)
    print("Air temperature: %.2f °C"% air_t)
    print("Soil temperature: %.2f °C " % soil_t)

    package = struct.pack('!f', float(air_t)) + struct.pack('!f', float(soil_t)) + struct.pack('!f', float(light))

    # make the socket blocking
    # (waits for the data to be sent and for the 2 receive windows to expire)
    s.setblocking(True)

    #define which port with the socket bind
    s.bind(2)

    #send some data
    s.send(package)

    s.setblocking(False)

    # get any data received...
    data = s.recv(64)
    print("Received from server: ", data)


while True:
    send_data()
    time.sleep(300)
