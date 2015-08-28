#!/usr/bin/python

from bootstrap import *

#setup colors for wipe
colors = [
	Color(255, 0, 0),
	Color(0, 255, 0),
	Color(0, 0, 255),
	Color(255, 255, 255),
]

for c in range(1):
	anim = ColorWipe(led, colors[c])

	for i in range(8):
		anim.step()
		led.update()
		sleep(0)
	

led.fillOff()
