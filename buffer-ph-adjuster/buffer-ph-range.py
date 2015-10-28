# Buffer pH adjuster
# www.scienceexposure.com
# Ismail Uddin, 2015
# This has sections adapted from the sample code provided by Atlas Scientific
# provided here: http://atlas-scientific.com/_files/code/pi_sample_code.pdf

from rrb2 import *
import serial
pH_range_upper = ("Please iput the upper value of pH you would like to set as a digit:")
pH_range_lower = ("Please iput the lower value of pH you would like to set as a digit:")
time_intvl = ("Please input the time interval for taking readings, in seconds:")

print("Press Ctrl-C to stop adjusting the pH")

# Initialising EZO pH circuit
usbport = '/dev/ttyAMA0'
ser = serial.Serial(usbport,9600)

# Initialize RaspiRobot board
rr = RRB2()

# pH meter readings
line = ""

pH_range = range(pH_range_lower, pH_range_upper)

def ph_reading():
	data = ser.read()
	if data == "/r":
		ph_value = float(line)
		line = ""
	else:
		line = line + data
	return ph_value

curr_ph = ph_reading()

while True:
	time.sleep(time_intvl)
	curr_ph = ph_reading()
	print("Current pH: %s" % curr_ph)
	

	if curr_ph < pH_range_lower:
		# Turn on pump supplying alkali
		rr.set_motors(0.25,0,0,0)
		print("Dispensing alkali...")
		time.sleep(0.35)
		rr.stop()

	elif curr_ph > pH_range_upper:
		# Turn on pump supplying acid_pump
		rr.set_motors(0,0,0.25,0)
		print("Dispensing acid...")
		time.sleep(0.35)
		rr.stop()
