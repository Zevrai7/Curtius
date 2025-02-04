import utime
from machine import I2C, Pin
from lib.mpu9250 import MPU9250

class ACCELEROMETER:
    def __init__(self):
        self.i2c = I2C(1, scl=Pin(19), sda=Pin(18))
        self.sensor = MPU9250(self.i2c)

    def printData(self):
        print(self.sensor.acceleration)
        print(self.sensor.gyro)
        print(self.sensor.temperature)

        utime.sleep_ms(1000)