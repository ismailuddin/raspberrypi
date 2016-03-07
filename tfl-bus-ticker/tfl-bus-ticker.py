# TfL Bus arrivals ticker
# Ismail Uddin, 2015
# www.scienceexposure.com

from TfLAPI import *
import Adafruit_CharLCD as LCD
import time
import sys

bSC = sys.argv[1]

#                 RS,EN,D4,D5,D6,D7,Co,Ro,BL
RPi_PIN_config = [27,22,25,24,23,18,16, 2, 4]
try:
	if  sys.argv[2] == "i2c":
		lcd = LCD.Adafruit_CharLCDPlate()
	else:
		lcd = LCD.Adafruit_CharLCD(*RPi_PIN_config)
except IndexError:
	lcd = LCD.Adafruit_CharLCD(*RPi_PIN_config)
	
lcd.clear()

lcd.message('Initialising...')
print('Initialising...')
lcd.show_cursor(True)
lcd.blink(True)
tfl = TfLBusArrivalsAPI()


lcd.clear()
lcd.message('Fetching TfL bus\narrivals...')
print('Fetching TfL bus\narrivals...')
lcd.blink(True)

def fetchBusArrivals():
	lcd.show_cursor(False)
	lcd.blink(False)
	try:
		jsonObject = tfl.returnTfLJSON(bus_stop_code=bSC)
	except urllib2.URLError:
		lcd.clear()
		print("Unable to connect to Internet...")
		lcd.message("Unable to connect \nto Internet...")
		
	busLineDestinationTime = []

	for entry in jsonObject:
		bLDT = []
		bLDT.append(entry['lineName'])
		bLDT.append(entry['destinationName'])
		bLDT.append(int(entry['timeToStation'])/60.0)
		busLineDestinationTime.append(bLDT)

	arrivalsList = sorted(busLineDestinationTime, key=lambda x:x[2])

	return arrivalsList


while True:
	arrivalsList = fetchBusArrivals()
	for bus in arrivalsList:
		lcd.clear()
		tickerInfo = '%s to %s \nin %.0f minutes' % (bus[0], bus[1], bus[2])
		lcd.message(tickerInfo)
		print(tickerInfo)
		time.sleep(3)
		for i in range(16):
			time.sleep(0.1)
			lcd.move_left()
