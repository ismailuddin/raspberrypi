# Buffer pH adjuster
# www.scienceexposure.com
# Ismail Uddin, 2015
# This has sections adapted from the sample code provided by Atlas Scientific
# provided here: http://atlas-scientific.com/_files/code/pi_sample_code.pdf

from rrb2 import *
import serial

print("Calibration will begin with ph solution 4, followed by 7 and 10")

# Initialising EZO pH circuit
usbport = '/dev/ttyAMA0'
ser = serial.Serial(usbport,9600)

# pH meter readings
line = ""

def ph_reading():
	data = ser.read()
	if data == "/r":
		ph_value = float(line)
		line = ""
	else:
		line = line + data
	return ph_value


curr_ph = ph_reading()

# Calibrating at pH 4
try:
	curr_ph = ph_reading()
	ser.write("cal,low,4\r")
	while curr_pH != 4:
		try:
			time.sleep(0.5)
			print("Current pH: %s" % curr_ph)
		finally:
			pass
finally:
	pass

# Calibrating at pH 7
try:
	curr_ph = ph_reading()
	ser.write("cal,mid,7\r")
	while curr_pH != 7:
		try:
			time.sleep(0.5)
			print("Current pH: %s" % curr_ph)
		finally:
			pass
finally:
	pass

# Calibrating at pH 10
try:
	curr_ph = ph_reading()
	ser.write("cal,high,10\r")
	while curr_pH != 10:
		try:
			time.sleep(0.5)
			print("Current pH: %s" % curr_ph)
		finally:
			pass
finally:
	pass
