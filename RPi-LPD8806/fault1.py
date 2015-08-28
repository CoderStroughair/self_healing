#!/usr/bin/python

from bootstrap import *

fault = 2

'''def __init__(self, led, start, end):
	self._led = led
	self._start = start
	self._end = end

section1 = (self._start == 0, end == 1)'''

if fault == 0:
	for c in range(1):
	
		anim = ColorWipe2(led, Color(0,150,0),0,50)
	

		for i in range(50):
			anim.step()
			led.update()
			sleep(0)

	for c in range(1):
	
		anim = ColorWipe2(led, Color(0,0,150),80,49)
	

		for i in range(31):
			anim.step()
			led.update()
			sleep(0)

elif fault == 1:
	led.fill(Color(0,0,0),0,50)
	led.fill(Color(0,0,150),50,80)
	led.update()
	sleep(1)
	led.fill(Color(150,0,0),0,50)
	led.update()
	sleep(1)

	for c in range(1):
	
		anim = ColorWipe2(led, Color(0,0,150),50,10)
	

		for i in range(40):
			anim.step()
			led.update()
			sleep(0)

elif fault == 2:
	led.fill(Color(0,0,0),10,50)
	led.fill(Color(0,150,0),0,10)
	led.fill(Color(0,0,150),50,80)
	led.update()
	sleep(1)
	led.fill(Color(150,0,0),10,50)
	led.update()
	sleep(1)

	for c in range(1):
	
		anim = ColorWipe2(led, Color(0,0,150),50,20)
	

		for i in range(30):
			anim.step()
			led.update()
			sleep(0)

elif fault == 3:
	led.fill(Color(0,0,0),20,50)
	led.fill(Color(0,150,0),0,20)
	led.fill(Color(0,0,150),50,80)
	led.update()
	sleep(1)
	led.fill(Color(150,0,0),20,50)
	led.update()
	sleep(1)

	for c in range(1):
	
		anim = ColorWipe2(led, Color(0,0,150),50,30)
	

		for i in range(20):
			anim.step()
			led.update()
			sleep(0)

elif fault == 4:
	led.fill(Color(0,0,0),30,50)
	led.fill(Color(0,150,0),0,30)
	led.fill(Color(0,0,150),50,80)
	led.update()
	sleep(1)
	led.fill(Color(150,0,0),30,50)
	led.update()
	sleep(1)

	for c in range(1):
	
		anim = ColorWipe2(led, Color(0,0,150),50,40)
	

		for i in range(10):
			anim.step()
			led.update()
			sleep(0)

elif fault == 5:
	led.fill(Color(0,0,0),40,50)
	led.fill(Color(0,150,0),0,40)
	led.fill(Color(0,0,150),50,80)
	led.update()
	sleep(1)
	led.fill(Color(150,0,0),40,50)
	led.update()
	sleep(1)

elif fault == 6:
	led.fill(Color(0,0,0),50,60)
	led.fill(Color(0,150,0),0,50)
	led.fill(Color(0,0,150),60,80)
	led.update()
	sleep(1)
	led.fill(Color(150,0,0),50,60)
	led.update()
	sleep(1)

elif fault == 7:
	led.fill(Color(0,0,0),50,70)
	led.fill(Color(0,150,0),0,50)
	led.fill(Color(0,0,150),70,80)
	led.update()
	sleep(1)
	led.fill(Color(150,0,0),50,70)
	led.update()
	sleep(1)

	for c in range(1):
	
		anim = ColorWipe2(led, Color(0,150,0),50,60)
	

		for i in range(10):
			anim.step()
			led.update()
			sleep(0)

elif fault == 8:
	led.fill(Color(0,0,0),50,80)
	led.fill(Color(0,150,0),0,50)
	
	led.update()
	sleep(1)
	led.fill(Color(150,0,0),50,80)
	led.update()
	sleep(1)

	for c in range(1):
	
		anim = ColorWipe2(led, Color(0,150,0),50,70)
	

		for i in range(20):
			anim.step()
			led.update()
			sleep(0)





