# sync
import time
from machine import Pin
from machine import I2C
import MAX44009
from onewire import DS18X20
from onewire import OneWire

# initialize I2C bus for ambient light sensor
i2c = I2C(0, I2C.MASTER)
i2c = I2C(0, pins=('P9','P10'))
i2c.init(I2C.MASTER, baudrate=10000)

# initialize ambient light sensor
lightsensor = MAX44009.MAX44009(i2c)
lightsensor.continuous = 1
lightsensor.manual = 0
lightsensor.current_division_ratio = 0
lightsensor.integration_time = 3

# Initialize OneWire bus for temp Sensor
# DS18B20 data line connected to pin P21
ow = OneWire(Pin('P21'))
temp = DS18X20(ow)

print("Starting measurements...")

while True:
    # Measure and print light
    read_lux = -1
    try:
        read_lux = lightsensor.lux_fast
    except:
        print("could not measure light")

    print("Ambient Light luminance : %.2f lux" % read_lux)

    # Measure and print ambient temperature
    print(temp.read_temp_async())
    time.sleep(2)
    temp.start_conversion()
    time.sleep(5)


############### junk code

"""
### CODE FOR lowercase library
import max44009

# i2c.scan() yields [74]
GY49_ADDR = 74


gy49 = max44009.MAX44009(address=74, i2c=i2c)


while True:

    time.sleep(1)
    gy49.measure()

    lux = gy49.read_value()

    print("Ambient Light luminance : %.2f lux" % lux)

    time.sleep(3)
"""
