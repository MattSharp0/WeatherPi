'''
Run this code on Pi 
'''

from os import wait
from PIL import Image
import time
import display
from inky.auto import auto


inky_display = auto()


img1 = Image.new(
    'P', (inky_display.WIDTH, inky_display.HEIGHT), inky_display.BLACK)

display.draw_temperature(img1)

inky_display.set_image(img1)
inky_display.show()
print('drawing temp page')

time.sleep(45)
img1.close()

img2 = Image.new(
    'P', (inky_display.WIDTH, inky_display.HEIGHT), inky_display.BLACK)

display.windvane(img2)

inky_display.set_image(img2)
inky_display.show()
print('drawing windvane page')
img2.close()
