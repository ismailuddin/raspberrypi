# Buffer pH adjuster
This code accompanies the 'Buffer pH adjuster' tutorial at www.scienceexposure.com. To use this code, you will need necessary accompanying hardware (listed in full detail on the tutorial page). This code allows you to build a project that monitors the pH of a solution, and adjusts it automatically by dispensing from an acid or alkali reservoir, to the pH value you have set.

The `calibrate.py` code is run once a day for calibrating the pH meter, and the `buffer-ph.py` is the main code for the project.

## Requirements
* Raspberry Pi (any model will do)
* PySerial 2.6
* Atlas Scientific pH kit
* RaspiRobot board v2
* Monk Makes 'RaspiRobot board' API (https://github.com/simonmonk/raspirobotboard2)

## Running the code
