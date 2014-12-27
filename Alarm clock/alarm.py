# Raspberry Pi Alarm Clock
# 2014, Ismail Uddin
# www.scienceexposure.com

import time
import RPi.GPIO as GPIO
from buzzer import buzz

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)

response = raw_input("Please input the time for the alarm in format HHMM: \n")

print("Alarm has been set for %s hrs" % response)
buzz(500,0.1)

alarm = int(response)
awake = 0

try:
    # Loop to continuously check time, buzz the buzzer for the set alarm time
    while True:
            # Continually get's the time as an integer value
            curr_time = int(time.strftime("%H%M"))

            # Buzzes the buzzer when the time reaches the set alarm time
            if timenow == alarm:
                    buzz(10,0.5)
                    time.sleep(0.25)
                    buzz(20,0.5)
                    time.sleep(0.25)
                    awake = 1

            # Snoozes the alarm for 8 minutes from the current time
            # Only works whilst the alarm is buzzing
            if GPIO.input(25) == 0 and awake == 1:
                    alarm += 8
                    awake = 0
                    print(alarm)

            # If alarm continues past the set alarm time without being
            # snoozed, the alarm time is changed to the current time.
            # This ensures the alarm buzzes continuously until the
            # snooze button is pressed.
            elif curr_time != alarm and awake == 1:
                    alarm = curr_time
                    buzz(10,0.5)
                    time.sleep(0.25)
                    buzz(20,0.5)

finally:
        GPIO.cleanup()
        print("End")
