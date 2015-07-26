from distutils.core import setup

setup(
    name = "LEDController",
    version = "0.1.1",
    author = "Ismail Uddin",
    author_email = "ismail.sameeuddin@gmail.com",
    license = "Apache 2.0",
    description = ("Collection of functions to control MAX7219 LED matrices using Python on Raspberry Pi"),
    long_description = """
    A small library of functions for controlling the LED matrices driven by the MAX7219 driver.
    Dependencies: max7219 (https://github.com/rm-hull/max7219)
    Complements the PyQt4 GUI LED controller.
    www.scienceexposure.com
    """,
    keywords = "raspberry pi led controller max7219",
    packages=['LEDController'],
    url = "https://github.com/ismailuddin/raspberrypi/led-matrix/",
)