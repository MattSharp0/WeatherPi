'''
Run this code on Pi 
'''

from os import wait
from PIL import Image, ImageDraw
import time
import display
from inky.auto import auto


inky_display = auto()

nightmode = True
if nightmode:
    base_color = inky_display.BLACK
else:
    base_color = inky_display.WHITE

temperature = Image.new(
    'P', (inky_display.WIDTH, inky_display.HEIGHT), base_color)

display.draw_temperature(temperature, nightmode)

inky_display.set_image(temperature)
inky_display.show()
print('drawing temp page')

time.sleep(90)
temperature.close()

windvane = Image.new(
    'P', (inky_display.WIDTH, inky_display.HEIGHT), base_color)

display.draw_windvane(windvane, nightmode)

inky_display.set_image(windvane)
inky_display.show()
print('drawing windvane page')
windvane.close()
