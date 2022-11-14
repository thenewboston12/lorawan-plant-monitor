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

# lightsensor.continuous = 1
# lightsensor.manual = 0
# lightsensor.current_division_ratio = 0
# lightsensor.integration_time = 3

# Initialize OneWire bus for temp Sensor
# DS18B20 data line connected to pin P21
ow1 = OneWire(Pin('P21'))
ow2 = OneWire(Pin('P22'))
air_temp = DS18X20(ow1)
soil_temp = DS18X20(ow2)


def measure():
    # Measure and print light
    read_lux = 0.0
    try:
        read_lux = lightsensor.lux_fast
    except:
        print("could not measure light")

    # Measure and print temperatures
    _air_t =  air_temp.read_temp_async()
    _soil_t = soil_temp.read_temp_async()
    _lux = read_lux
    time.sleep(2)
    air_temp.start_conversion()
    soil_temp.start_conversion()
    time.sleep(5)

    return _air_t, _lux, _soil_t
