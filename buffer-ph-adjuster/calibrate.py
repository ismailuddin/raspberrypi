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

# Calibrating at pH 4
try:
	curr_ph = ph_reading()
	ser.write("cal,low,4\r")
	while True:
		try:
			time.sleep(0.5)
			print("Current pH: %s" % curr_ph)
		except:
			pass
except:
	pass


