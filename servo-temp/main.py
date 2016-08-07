import max7219.led as led 
from temp import *
from servosix import ServoSix 
import time

ss = ServoSix()
device = led.matrix()
device.orientation(180)

min_temp, max_temp = 15, 45
min_servo, max_servo = 0, 180


def servoScale(val):
	temp_range = (max_temp - min_temp)
	servo_range = (max_servo - min_servo)

	servo_val = (((val - min_temp)*servo_range) / temp_range) + min_servo
	return servo_val

while True:
	time.sleep(1)
	temp = temp_from_r(read_resistance())
	device.show_message("{0:0.0f}".format(temp))
	s = servoScale(temp)
	ss.set_servo(1, (180-s))
	print("{0:0.0f}".format(temp))
