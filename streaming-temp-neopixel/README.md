# Neopixel LED temperature gauge

This script accompanies the 'Neopixel LED temperature gauge' project at www.scienceexposure.com. The primary file `main.py` contains the bulk of the code, that runs the project. Temperature readings are calculated from the thermistor using the `temp.py` file, which contains code part of the Monk Makes Raspbery Pi Starter Kit project. The `config.json` file houses the credentials for enabling plotting the temperature values in real time.

## Requirements
* Raspberry Pi model B, B+ or A (Pi 2 is not supported by one of the libraries required for this project)
* Internet access to the Raspberry Pi for real time plotting (not obligatory)
* Adafruit Neopixel RGB 12 LED
* Monk Makes Starter Kit (or suitable temperature sensor)

## How to run the code
Before running the code, a number of libraries must be installed beforehand. Please the blog post on www.scienceexposure.com for details.

To run the code without plotting temperature values, type `sudo python main.py run`.

To run the code with plotting temperatures values to Plot.ly, type `sudo python main.py plotly`.
