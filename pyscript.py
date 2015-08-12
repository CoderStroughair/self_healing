import RPi.GPIO as GPIO
import os
from bibliopixel.drivers.visualizer import *
from bibliopixel.led import *
from bibliopixel.animation import *
from matrix_animations import *
from strip_animations import *

driver = DriverLPD8806(100, c_order = ChannelOrder.RGB, use_py_spi = True, dev="/dev/spidev0.0", SPISpeed = 10)
GPIO.setmode(GPIO.BOARD);
GPIO.setup(1, GPIO.IN);

def setup():
	#### A function that sets the LEDs up to the resting configuration, ie, Green on the left, and Blue on the right




while true:
	GPIO.wait_for_edge(1, GPIO.RISING);		#waiting for someone to press the button that triggers a fault
	# Turn off relevant LEDs #
	# Done by flashing the fault zone red to show where it is, then turning the rest of the affected LEDs red as well.
	
	sleep(5);
	# Start turning on the LEDs, line by line, in the new colour, at maybe one segment every 2 seconds #
	
	sleep(15);
	#Reset the board back to the original configuration
	