#!/usr/bin/python
import webiopi
import datetime
import os

GPIO = webiopi.GPIO
os.chdir("/home/pi/RPi-LPD8806/")
from bootstrap import *


def setup():
	# set the GPIO used by the light to output
	
	fault = 6
	lFault = 0

	nOpen = 4

	open1 = 0
	open2 = 0

	segment = [0,20,40,60,80,100,120,140,160]

	led.fill(Color(0,255,0),segment[0],segment[nOpen])
	led.fill(Color(0,0,255),segment[nOpen]+1,segment[len(segment) - 1])
	led.update()
	sleep(1)


# loop function is repeatedly called by WebIOPi 
def loop():
	
	# gives CPU some time before looping again
	webiopi.sleep(1)

# destroy function is called at WebIOPi shutdown
def destroy():
	GPIO.digitalWrite(LIGHT, GPIO.LOW)

@webiopi.macro
def getLightHours():
	return "%d;%d" % (fault, open1)

@webiopi.macro
def setLightHours(on, off):
	global fault, open1
	fault = int(on)
	open1 = int(off)
	if fault >= 1:
		for i in range(11):
			led.fill(Color(255*(i%2),0,0),segment[fault - 1] + ((segment[fault] - segment[fault -1])/2), segment[fault - 1] + ((segment[fault] - segment[fault -1])/2)+1)
			led.update()
			sleep(.2)
			i += 1


		if fault <= nOpen:


			'''led.fill(Color(0,0,255),segment[nOpen],segment[len(segment) - 1])
			led.update()
			sleep(0)'''



			led.fill(Color(255,0,0),segment[fault - 1], segment[fault])
			led.update()
			sleep(1)

		

			anim = ColorWipe2(led, Color(0,0,0),segment[fault]+1,segment[nOpen]+1)
	
	
			for i in range(segment[nOpen] - segment[fault]+1):
				anim.step()
				led.update()
				sleep(0)

			led.fill(Color(0,0,0),segment[fault - 1], segment[fault])
			led.fill(Color(255,0,0),segment[fault - 1] + ((segment[fault] - segment[fault -1])/2), segment[fault - 1] + ((segment[fault] - segment[fault -1])/2)+1)
			led.update()
			sleep(1)

			#Fault sequence over	
		
			anim = ColorWipe2(led, Color(0,0,255),segment[nOpen],segment[fault - 1] + ((segment[fault] - segment[fault -1])/2)+1)
		
	
			for i in range(segment[nOpen] - segment[fault - 1] + ((segment[fault] - segment[fault -1])/2)+1):
				anim.step()
				led.update()
				sleep(0)

			for i in range(10):
				led.fill(Color(255*(i%2),0,0),segment[fault - 1] + ((segment[fault] - segment[fault -1])/2), segment[fault - 1] + ((segment[fault] - segment[fault -1])/2)+1)
				led.update()
				sleep(.2)
				i += 1

			anim = ColorWipe2(led, Color(0,0,0),segment[fault - 1] + ((segment[fault] - segment[fault -1])/2)+2,segment[fault] + 1)
	
	
			for i in range(segment[fault] - segment[fault] + ((segment[fault] - segment[fault - 1])/2)+2):
				anim.step()
				led.update()
				sleep(0)



		else:


			'''led.fill(Color(0,255,0),segment[0],segment[nOpen])
			led.update()
			sleep(0)'''


			led.fill(Color(255,0,0),segment[fault - 1], segment[fault])
			led.update()
			sleep(1)

			anim = ColorWipe2(led, Color(0,0,0),segment[fault - 1]-1,segment[nOpen])
	
	
			for i in range(segment[fault - 1] - segment[nOpen]):
				anim.step()
				led.update()
				sleep(0)

			led.fill(Color(0,0,0),segment[fault - 1], segment[fault])
			led.fill(Color(255,0,0),segment[fault - 1] + ((segment[fault] - segment[fault -1])/2), segment[fault - 1] + ((segment[fault] - segment[fault -1])/2)+1)
			led.update()
			sleep(1)




			anim = ColorWipe2(led, Color(0,255,0),segment[nOpen],segment[fault - 1] + ((segment[fault] - segment[fault -1])/2))
	
	
			for i in range(segment[fault - 1] + ((segment[fault] - segment[fault -1])/2)+1 - segment[nOpen]):
				anim.step()
				led.update()
				sleep(0)

			for i in range(10):
				led.fill(Color(255*(i%2),0,0),segment[fault - 1] + ((segment[fault] - segment[fault -1])/2), segment[fault - 1] + ((segment[fault] - segment[fault -1])/2)+1)
				led.update()
				sleep(.2)
				i += 1

			anim = ColorWipe2(led, Color(0,0,0),segment[fault] + ((segment[fault] - segment[fault + 1])/2)-1,segment[fault-1]-1)
	
	
			for i in range(segment[fault] + ((segment[fault] - segment[fault + 1])/2)+2 - segment[fault-1]):
				anim.step()
				led.update()
				sleep(0)
		return getLightHours()









