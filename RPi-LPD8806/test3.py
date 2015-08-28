#!/usr/bin/python

from bootstrap import *

#led.all_off()

#led.fill(Color(160,60,60),20,160)
#led.update()

#setup colors for wipe
colors = [
	Color(255, 0, 0),
	Color(0, 255, 0),
	Color(0, 0, 255),
	Color(255, 255, 255),
]

for c in range(1):
	
	anim = ColorWipe2(led, Color(100,0,0),40,20)
	

	for i in range(20):
		anim.step()
		led.update()
		sleep(0)

	anim = ColorWipe2(led, Color(0,0,100),10,21)

	for i in range(11):
		anim.step()
		led.update()
		sleep(0)
	
	

