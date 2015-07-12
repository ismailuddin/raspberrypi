from xml.dom import minidom
import urllib2
import time
import RPi.GPIO as GPIO
from neopixel import *

# LED strip configuration:
LED_COUNT      = 12      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 60      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

lastButton = False
GPIO.setmode(GPIO.BCM)
switchPin = 25

GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

linestatus_dict = {}

def update_underground_status():
	xmlfile = urllib2.urlopen('http://cloud.tfl.gov.uk/TrackerNet/LineStatus')
	parsed = minidom.parse(xmlfile)
	linestatus = parsed.getElementsByTagName("LineStatus")

	for entry in linestatus:
	    line = entry.getElementsByTagName("Line")
	    name = line[0].getAttribute("Name")
	    status_details = entry.getAttribute("StatusDetails")
	    if status_details != '':
	        linestatus_dict[str(name)] = 1
	    else:
	        linestatus_dict[str(name)] = 0
	parsed, linestatus, line, name, status_details = None, None, None, None, None
	return linestatus_dict


uc = {
		'Bakerloo':[50,18,0],
		'Central':[229,0,0],
		'Circle':[255,255,0],
		'DLR':[134,253,215],
		'District':[0,255,0],
		'Hammersmith and City':[255,192,203],
		'Jubilee':[60,60,60],
		'Metropolitan':[128,0,128],
		'Northern':[10,10,10],
		'Overground':[255,165,0],
		'Piccadilly':[30,30,102],
		'Victoria':[40,220,255],
		'Waterloo and City':[0,255,255],
		'TfL Rail':[53,92,125]
}

def reset():
	for i in range(0,12):
		strip.setPixelColorRGB(i,0,0,0)
		strip.show()

def neopixel_status(ugline):
	if linestatus_dict[str(ugline)] == 0:
		reset()
		for i in range(0,12):
			strip.setPixelColorRGB(i,uc[str(ugline)][0],uc[str(ugline)][1],uc[str(ugline)][2])
			strip.show()
	else:
		reset()
		for i in range(0,12,2):
			strip.setPixelColorRGB(i,uc[str(ugline)][0],uc[str(ugline)][1],uc[str(ugline)][2])
			strip.show()
	print(str(ugline))

i = 0

def next_line():
	global i
	if i >= (len(line_names)-1):
		i = 0
	else:
		i += 1
	return line_names[i]

if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()
	strip.setBrightness(25)

	update_underground_status()
	line_names = linestatus_dict.keys()
	curr_line = line_names[0]
	neopixel_status(curr_line)
	print curr_line
	try:
		while True:
			if GPIO.input(switchPin) == 0:
				update_underground_status()
				line_names = linestatus_dict.keys()
				curr_line = next_line()
				neopixel_status(curr_line)
			else:
				pass
	finally:
		pass