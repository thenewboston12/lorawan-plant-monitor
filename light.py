from machine import I2C
import time
import MAX44009


i2c = I2C(0, I2C.MASTER)

i2c = I2C(0, pins=('P9','P10'))

i2c.init(I2C.MASTER, baudrate=10000)



sensor = MAX44009.MAX44009(i2c)
sensor.continuous = 1
sensor.manual = 0
sensor.current_division_ratio = 0
sensor.integration_time = 3

while True:
    time.sleep(1)
    read_lux = -1
    try:
        read_lux = sensor.lux_fast
    except:
        print("could not measure light")

    print("Ambient Light luminance : %.2f lux" % read_lux)

    time.sleep(3)


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
