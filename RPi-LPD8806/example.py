#!/usr/bin/python

from bootstrap import *

#scanner: single color and changing color
#anim = LarsonScanner(led, Color(255, 0, 0))
#for i in range(132):
#	anim.step()
#	led.update()
#	#sleep(0.1)

#led.fillOff()
led.fill(Color(255,0,0), 0,143)
led.update()