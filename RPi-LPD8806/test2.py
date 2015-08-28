if c > 384:
		c=0.0
	height = height - 9.0
	height = height / 5

	if height < 0.05:
		height = 0.05
	if height > 1.0:
		height = 1.0
	
	if height < columns[col]:
		columns[col] = columns[col] *decay
		height = columns[col]
	else:
		columns[col] = height
	if col == 0:
		led.fill(color,0,int(round(height*25)))
	elif col == 1:
		led.fill(color,56 - int(round(height*25)),56)
	elif col == 2:
		led.fill(color,62,62+int(round(height*25)))
	elif col == 3:
		led.fill(color,118- int(round(height*25)),118)
	elif col == 4:
		led.fill(color,123,123+int(round(height*25)))
