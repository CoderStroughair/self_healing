#This Python scipt was created by Michael Stroughair for the ESB's self healing Network Model#
#As of Monday 24th August, this code has not ben tested with hardware, but the functionality is quite simple. When setting up the display board,
#Count the number of LEDs in each section, and update the Array below named sectionStart with the new values, along with the end value for the Green LEDs.
#Also note, this code is set up so that the first LED is the one closest to Cahircivee, so if the hardware is still not setup at time of reading, be sure
#to wire the LEDs in the correct way, or else you will need to change the values of the LEDs in this code to match.


import RPi.GPIO as GPIO
import os
from bootstrap import 

driver = DriverLPD8806(100, c_order = ChannelOrder.RGB, use_py_spi = True, dev="/dev/spidev0.0", SPISpeed = 10)
GPIO.setmode(GPIO.BOARD);
GPIO.setup(1, GPIO.IN);
ledEnd = 30;					#The number of green LEDs
sectionStart = [10,15,20,25,38,45,49];		#An array that holds the number of the starting LED for each section

def fWrite(time):	#A function that updates the file that the HTML page takes values from
	with open("time.html","w") as f:
		f.write("<link href='style.css' rel = 'stylesheet'<h1 style = 'color: white; font-family: 'Verdana'; text-align: center;'>Time Elapsed:");
		f.write(time);
		f.write("ms</h1>");

def setup():		#A function that sets the LEDs up to the resting configuration, ie, Green on the left, and Blue on the right 
	led.fill(Color(0, 0, 255), ledEnd, 1000);			#Fills the first set of LEDs with a Blue color
	led.fill(Color(0, 255, 0), 0, ledEnd-1);			#Fills the second set of LEDs with a Green color
	fWrite("9");							#Time is set to the waiting state, which triggers the html page to hide some components
	for i in range(7):
		led.fill(Color(0,145,96), sectionStart[i], sectionStart[i]);	#lights the Semaphores in a different color to the others. Probably worth changing later.
	led.update();
	
def refill(start, end):	#A function that will fill from the selected start and end point with Blue, simulating the recovery element of the Network
	led.fill(Color(0,15,25), start, start);				#Changes the color of the Semaphore
	led.update();							
	var anim = led.ColorWipe(led, Colour(0,0,255), start+1, end);	#Changes the color of the other LEDs in step.
	for i in range(5):
		anim.step();
		led.update();
		sleep(0);

setup();
while true:
	GPIO.wait_for_edge(1, GPIO.RISING);					#waiting for someone to press the button that triggers a fault

	var anim = led.ColorWipe2(led, Color(0,150,0),sectionStart[0],ledEnd);	#Turns damaged set of LEDs to red, indicating a fault
	for i in range(50):
		anim.step();
		led.update();
		sleep(0);
	fWrite("0");
	sleep(5);
	
	refill(sectionStart[0], sectionStart[1]-1);
	fWrite("1");
	sleep(5);
	refill(sectionStart[1],sectionStart[2]-1);
	fWrite("2");
	sleep(5);
	refill(sectionStart[2], sectionStart[3]-1);
	fWrite("3");
	sleep(5);
	refill(sectionStart[3], ledEnd-1);	
	fWrite("4");
	sleep(15);
	#Reset the board back to the original configuration
	setup();
