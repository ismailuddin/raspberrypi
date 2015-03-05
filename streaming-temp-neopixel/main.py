# Neopixel LED temperature gauge
# Real time plotting through Plotly
# www.scienceexposure.com

import time
from neopixel import *
import sys

plotting = sys.argv[1]

# LED strip configuration:
LED_COUNT      = 12     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 60     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

import random
from temp import *

def reset():
	for i in range(strip.numPixels()):
		strip.setPixelColorRGB(i,0,0,0)

def colour(temp):
	if temp < 18:
		reset()
		l = int((temp/18)*4)
		for i in range(0,l):
			# Cyan colour for low temperatures
			strip.setPixelColorRGB(i,0,255,255) 
			strip.show()
	elif temp < 24:
		reset()
		l = int(temp - 14)
		for i in range(0,l):
			# Green colour for medium temperatures
			strip.setPixelColorRGB(i,50,205,50)
			strip.setBrightness(25)
			strip.show()
	elif temp < 35:
		reset()
		l = int(((3/10.0)*temp) + 1.5)
		for i in range(0,l):
			# Red colour for high temperatures
			strip.setPixelColorRGB(i,255,0,0)
			strip.show()

if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print 'Press Ctrl-C to close the script.'

	if plotting == 'plotly':

		import plotly.plotly as py
		import json
		import datetime

		with open('./config.json') as config_file:
			plotly_user_config = json.load(config_file)
			py.sign_in(plotly_user_config["plotly_username"], plotly_user_config["plotly_api_key"])

		url = py.plot([
			{
				'x' : [], 'y' : [], 'type': 'scatter',
				'stream': {
					'token': plotly_user_config['plotly_streaming_tokens'][0],
					'maxpoints': 200
				}
			
		}], filename='RPi streaming temperature')

		print("View your streaming graph here:", url)

		stream = py.Stream(plotly_user_config['plotly_streaming_tokens'][0])
		stream.open()

	while True:
		t = temp_from_r(read_resistance())
		print(t)
		colour(t)
		if plotting == 'plotly':
			stream.write({'x': datetime.datetime.now(), 'y':t})		
		else:
			pass
		time.sleep(0.25)
