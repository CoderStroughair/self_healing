import RPi.GPIO as GPIO
import os
from bootstrap import 

driver = DriverLPD8806(100, c_order = ChannelOrder.RGB, use_py_spi = True, dev="/dev/spidev0.0", SPISpeed = 10)
GPIO.setmode(GPIO.BOARD);
GPIO.setup(1, GPIO.IN);

def fWrite(time):
	with open("time.html","w") as f:
		f.write("<link href='style.css' rel = 'tylesheet'<h1 style = 'color: white; font-family: 'Verdana'; text-align: center;'>Time Elapsed:");
		f.write(time);
		f.write("ms</h1>");

def setup():
	#### A function that sets the LEDs up to the resting configuration, ie, Green on the left, and Blue on the right
	###currently have 
	led.fill(Color(255, 0, 0), 0, 30);		#Fills the first 30 LEDs with a Green color
	led.fill(Color(0, 0, 255), 30, 60);		#Fills the second 30 LEDs with a Blue color
	fWrite("9");								#Time is set to the waiting state
	led.update();
	
def refill(start, end):
	var anim = led.ColorWipe(led, Colour(0,0,255), start, end);
	for i in range(5):
		anim.step()
		led.update()
		sleep(0)

setup();
while true:
	GPIO.wait_for_edge(1, GPIO.RISING);		#waiting for someone to press the button that triggers a fault

	var anim = led.ColorWipe2(led, Color(0,150,0),10,30);		#Turns damaged set of LEDs to red, indicating a fault
	for i in range(50):
			anim.step()
			led.update()
			sleep(0)
	fWrite("0");
	sleep(5);
	
	refill(10, 15);
	fWrite("1");
	sleep(5);
	refill(15, 20);
	fWrite("2");
	sleep(5);
	refill(20, 25);
	fWrite("3");
	sleep(5);
	refill(25, 30);	
	fWrite("4");
	sleep(15);
	#Reset the board back to the original configuration
	setup();