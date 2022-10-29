from network import LoRa
import socket
import time
import ubinascii
import struct
import pycom
import keys

# Initialise LoRa in LORAWAN mode.
# Europe = LoRa.EU868
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

# Colors
off = 0x000000
red = 0x7f0000
green = 0x007f00
blue = 0x00007f

# Turn off hearbeat LED
pycom.heartbeat(False)


# 70B3D5499B6E0541
print("DevEUI: " + ubinascii.hexlify(lora.mac()).decode('utf-8').upper())

#APP_EUI 0000000000000000
#APP_KEY A9BE60045BB1C51412D19B96CCB65007
# create an OTAA authentication parameters
app_eui = ubinascii.unhexlify(keys.APP_EUI)
app_key = ubinascii.unhexlify(keys.APP_KEY)


def connect_lorawan():
    # join a network using OTAA (Over the Air Activation)
    lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
    pycom.rgbled(red)

    while not lora.has_joined():
        print('Not yet joined...')
        pycom.rgbled(red)
        time.sleep(3)
        pycom.rgbled(off)
        time.sleep(0.5)

    print("Joined LoRaWAN network")

    pycom.rgbled(green)
    time.sleep(1)
    pycom.rgbled(off)
    time.sleep(0.5)


    # create socket to be used for LoRa communication and make it global
    global s
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

    # configure data rate SET 5 to 0 to get better range
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
