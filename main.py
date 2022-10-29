import sensors
import lorawan
import struct
import pycom
import time

# Colors
off = 0x000000
red = 0x7f0000
green = 0x007f00
blue = 0x00007f

# connect to network
lorawan.connect_lorawan()

# Socket to use for sending data
from lorawan import s

def send_data():
    air_t, light, soil_t = sensors.measure()

    if light is None :
        light = -1.0
        print("light measurement error")
    if air_t is None :
        print("Air temp measurement error")
        air_t = -273.0
    if soil_t is None :
        print("Soil temp measurement error")
        soil_t = -273.0


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
    print("Sent the measurements")
    pycom.rgbled(green)
    time.sleep(5)
    pycom.rgbled(off)


    s.setblocking(False)

    # get any data received...
    data = s.recv(64)
    print("Received from server: ", data)


while True:
    send_data()
    # Sleep for 5 minutes
    time.sleep(10*60)
