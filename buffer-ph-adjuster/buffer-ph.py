# Buffer pH adjuster
# www.scienceexposure.com
# Ismail Uddin, 2015
# This has sections adapted from the sample code provided by Atlas Scientific
# provided here: http://atlas-scientific.com/_files/code/pi_sample_code.pdf

from rrb2 import *
import serial
rr = RRB2()

# pH value to set buffer at
ph_set = ("Input the value of pH you would like set as a digit:")
print("Press Ctrl-C to stop adjusting the pH")

# Initialising EZO pH circuit
usbport = '/dev/ttyAMA0'
ser = serial.Serial(usbport,9600)



def ph_reading():
	# pH meter readings
	line = ""
	data = ser.read()
	if data == "/r":
		ph_value = float(line)
		line = ""
	else:
		line = line + data
	return ph_value

curr_ph = ph_reading

while ph_set != curr_ph:
	curr_ph = ph_reading()
	print("Current pH: %s" % curr_ph)

	if curr_ph < ph_set:
		# Turn on pump supplying alkali
		rr.set_motors(0.25,0,0,0)
		print("Dispensing alkali...")
		time.sleep(0.35)
		rr.stop()

	elif curr_ph > ph_set:
		# Turn on pump supplying acid_pump
		rr.set_motors(0,0,0.25,0)
		print("Dispensing acid...")
		time.sleep(0.35)
		rr.stop()

	time.sleep(0.5)

