# from https://github.com/cpla33/max44009/blob/master/max44009.py
import time

# MAX44009 default address
MAX44009_I2CADDR = 0x4A

class MAX44009:
    def __init__(self, address=MAX44009_I2CADDR, i2c=None, **kwargs):
        self.address = address
        if i2c is None:
            raise ValueError('An I2C object is required.')
        self.i2c = i2c

    # Write buf (0x40) to the configuration register (0x02)
    # 0x40(64) sets Continuous mode, Integration time = 800 ms
    def measure(self):
        # self.i2c.writeto_mem(self.address, 0x02, bytearray([0x40]))
        self.i2c.writeto_mem(self.address, 0x02, bytes([0x40]))
        time.sleep(0.5)

    # Read 2 bytes from the measured data storage register (0x03)
    # Returns a bytes object with the data read
    def read_value(self):
        data = self.i2c.readfrom_mem(self.address, 0x03, 2)

        exponent = (data[0] & 0xF0) >> 4
        mantissa = ((data[0] & 0x0F) << 4) | (data[1] & 0x0F)
        luminance = ((2 ** exponent) * mantissa) * 0.045

        return luminance
