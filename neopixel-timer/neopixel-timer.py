# 2015, Ismail Uddin
# www.scienceexposure.com

from threading import Thread
import random
import sys
import RPi.GPIO as GPIO
import time
from potentiometer import *

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)

from neopixel import *

# LED strip configuration:
LED_COUNT   = 12      # Number of LED pixels.
LED_PIN     = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA     = 5       # DMA channel to use for generating signal (try 5)
LED_INVERT  = False   # True to invert the signal (when using NPN transistor level shift)

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)
# Intialize the library (must be called once before other functions).
strip.begin()
strip.setBrightness(50)
strip.show()



low_end = 19
high_end = 251
pot_range = high_end - low_end
smallest_unit = pot_range / 11

currentNumber = 0
timerValue = 0
setTimerMode = True
timerCountdownMode = True
alarmMode = False



def neopixel_number():
	resistance = analog_read()
	number = (resistance / smallest_unit) + 1
	return number

def updateNeopixels(number, color):
	global currentNumber
	if number != currentNumber:
		for i in range(0,strip.numPixels()):
			strip.setPixelColorRGB(i,0,0,0)
			strip.show()
		print(number)
		for i in range(0, number):
			strip.setPixelColorRGB(i,color[0],color[1],color[2])
			strip.show()
		currentNumber = number

def loopForButton():
	global setTimerMode
	global timerValue
	while setTimerMode == True:
		if GPIO.input(25) == 0:
			timerValue = neopixel_number()
			print("Timer set for %s minutes" % timerValue)
			setTimerMode = False
		else:
			pass
	time.sleep(0.1)

def alarmAnimation():
	strip.setBrightness(128)
	for i in range(strip.numPixels()):
		r = random.randrange(0,255)
		g = random.randrange(0,255)
		b = random.randrange(0,255)
		strip.setPixelColorRGB(i,r,g,b)
		strip.show()
		time.sleep(0.1)


def mainLoop():
	global timerCountdownMode
	global alarmMode
	while timerCountdownMode == True:
		if setTimerMode == True:
			newNumber = neopixel_number()
			updateNeopixels(newNumber,[30,30,102])
			time.sleep(0.5)
		elif setTimerMode == False and alarmMode == False:
			strip.setBrightness(25)
			updateNeopixels(timerValue, [0,255,0])
			print("Started loop")
			time.sleep(timerValue * 10)
			print("Stuck in loop")
			alarmAnimation()
			alarmMode = True
		elif setTimerMode == False and alarmMode == True:
			alarmAnimation()
			if GPIO.input(25) == 0:
				print("Exiting program")
				for i in range(strip.numPixels()):
					strip.setPixelColorRGB(i,0,0,0)
					strip.show()
				sys.exit()
		else:
			pass

if __name__ == "__main__":
	try:
		t1 = Thread(target=mainLoop)
		t1.daemon = True
		t1.start()
		t2 = Thread(target=loopForButton)
		t2.daemon = True
		t2.start()
		while True:
			time.sleep(100)
	except (KeyboardInterrupt, SystemExit):
		print("End")

