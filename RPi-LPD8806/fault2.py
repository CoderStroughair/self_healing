#!/usr/bin/python
import webiopi
import datetime
import os

GPIO = webiopi.GPIO
from bootstrap import *

lFault = 0
reclosers = [0,0,0,0,0,0,0,0,0]
first = -1
last = -1
for j in range(len(reclosers)):
	file = open('//home/pi/R' + str(j+1) + '.txt', 'r')
	reclosers[j] = int(file.readline())
	file.close()
	if reclosers[j] == 2: # operational
		if lFault != 1:
			lFault = -1
		if first == -1:
			first = j # sets first
			section = first
			nOpen = first
			last = first 
		elif first > -1:
			last = j  # sets last fault
			nOpen = last
	elif reclosers[j] == 1: # fault
		lFault = 1 # identify fault
		fault = j+1
		section = fault

segment = [0,35,43,55,71,83,93,105,141]

#NO FAULT
if lFault < 0: # Operational change
	#led.fill(Color(0,0,0),0,143)
	#led.fill(Color(255,0,0),first,last)
	#led.update()
	#sleep(5)
	for i in range(12):
		led.fill(Color(0,255,0),segment[0],segment[first])
		led.fill(Color(255*(i%2),0,0),segment[first]+1,segment[last])	
		led.fill(Color(0,0,255),segment[last]+1,segment[8])
		led.update()
		sleep(0.2)	
	#reclosers[segment-1] = 2
	
elif lFault == 0: # Restore
	reclosers = [0,0,0,0,2,0,0,0,0]
	led.fill(Color(0,255,0),segment[0],segment[5])
	led.fill(Color(0,0,255),segment[5]+1,segment[8])
	led.update()
	sleep(1)
#DEFINATELY FAULT
elif lFault == 1:
	nOpen = 4
	reclosers = [0,0,0,0,0,0,0,0,0]
	reclosers[fault-1] = 1
	reclosers[fault] = 2
	led.fill(Color(0,255,0),segment[0],segment[nOpen]) # set GREEN
	led.fill(Color(0,0,255),segment[nOpen]+1,segment[len(segment) - 1]) # set BLUE
	led.update() # OUTPUT
	#there is a fault and now act on it
	if fault >= 1:
		for i in range(11):
			led.fill(Color(255*(i%2),0,0),segment[fault - 1] + ((segment[fault] - segment[fault -1])/2), segment[fault - 1] + ((segment[fault] - segment[fault -1])/2))
			led.update() # flash LED 5 times
			sleep(0.1)
			i += 1

		if fault <= nOpen: # before NOpen
	#		file = open('//home/pi/workfile2.txt', 'w')
	#		file.write("1\n" + str(nOpen) + "\n" + str(fault) + "\n")
	#		file.close()
			for i in range(6):
				led.fill(Color(255*(i%2),0,0),segment[fault - 1]+1, segment[nOpen])
				led.update()
				sleep(0.2)
				i += 1 # flash segment 5 times

			led.fill(Color(255,0,0),segment[fault]+1,segment[nOpen])
			led.update() # turn of segment

			for i in range(3):
				led.fill(Color(255,0,0),segment[fault - 1]+1, segment[fault])
				led.update()
				sleep(0.1)
				led.fill(Color(0,0,0),segment[fault - 1]+1, segment[fault])
				led.fill(Color(255,0,0),segment[fault - 1] + ((segment[fault] - segment[fault -1])/2), segment[fault - 1] + ((segment[fault] - segment[fault -1])/2))
				led.update()
				sleep(3)
			#Fault sequence over	RESTORE time
			anim = ColorWipe2(led, Color(0,0,255),segment[nOpen],segment[fault-1])
			for i in range(segment[nOpen] - segment[fault-1]+1):
				anim.step()
				led.update()

			for i in range(10):
				led.fill(Color(255*(i%2),0,0),segment[fault - 1] + ((segment[fault] - segment[fault -1])/2), segment[fault - 1] + ((segment[fault] - segment[fault -1])/2))
				led.update() # flash fault location
				sleep(.2)
				i += 1

			for i in range(4):
				led.fill(Color(255,0,0),segment[fault - 1]+1, segment[fault])
				led.update()
				sleep(0.1)
				led.fill(Color(0,0,0),segment[fault - 1]+1, segment[fault])
				led.fill(Color(255,0,0),segment[fault - 1] + ((segment[fault] - segment[fault -1])/2), segment[fault - 1] + ((segment[fault] - segment[fault -1])/2))
				led.update()
				sleep(3)
			led.fill(Color(0,0,0),segment[fault - 1]+1, segment[fault])
			led.update()
			led.fill(Color(255,0,0),segment[fault - 1] + ((segment[fault] - segment[fault -1])/2), segment[fault - 1] + ((segment[fault] - segment[fault -1])/2))
			led.update()

		else: # beyond NOpen
	#		file = open('//home/pi/workfile2.txt', 'w')
	#		file.write("1\n" + str(fault) + "\n" + str(nOpen) + "\n")
	#		file.close()
			for i in range(6):
				led.fill(Color(255*(i%2),0,0),segment[nOpen]+1, segment[fault])
				led.update()
				sleep(0.2)
				i += 1 # flash segment

			led.fill(Color(255,0,0),segment[nOpen]+1,segment[fault - 1]-1)
			led.update()

			led.fill(Color(0,0,0),segment[fault - 1]+1, segment[fault])
			led.fill(Color(255,0,0),segment[fault - 1] + ((segment[fault] - segment[fault -1])/2), segment[fault - 1] + ((segment[fault] - segment[fault -1])/2))
			led.update() # illuminate fault
			
			for i in range(3):
				led.fill(Color(255,0,0),segment[fault - 1]+1, segment[fault])
				led.update()
				sleep(0.1)
				led.fill(Color(0,0,0),segment[fault - 1]+1, segment[fault])
				led.fill(Color(255,0,0),segment[fault - 1] + ((segment[fault] - segment[fault -1])/2), segment[fault - 1] + ((segment[fault] - segment[fault -1])/2))
				led.update()
				sleep(3)

			# fault over
			anim = ColorWipe2(led, Color(0,255,0),segment[nOpen],segment[fault]+1)

			for i in range(segment[fault] - segment[nOpen]+1):
				anim.step()
				led.update()

			for i in range(10):
				led.fill(Color(255*(i%2),0,0),segment[fault - 1] + ((segment[fault] - segment[fault -1])/2), segment[fault - 1] + ((segment[fault] - segment[fault -1])/2))
				led.update()
				sleep(0.2)
				i += 1

			for i in range(6):
				led.fill(Color(255,0,0),segment[fault - 1]+1, segment[fault])
				led.update()
				sleep(0.1)
				led.fill(Color(0,0,0),segment[fault - 1]+1, segment[fault])
				led.fill(Color(255,0,0),segment[fault - 1]+1, segment[fault])
				led.update()
				sleep(2)
			#led.fill(Color(0,0,0),segment[fault],segment[fault-1])
			#led.update()
			#led.fill(Color(255,0,0),segment[fault - 1] + ((segment[fault] - segment[fault -1])/2), segment[fault - 1] + ((segment[fault] - segment[fault -1])/2))
			#led.update()
		
for k in range(len(reclosers)):
	file = open('//home/pi/R' + str(k+1) + '.txt', 'w')
	file.write(str(reclosers[k]))
	file.close()
