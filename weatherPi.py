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

display.temperature(img1)

inky_display.set_image(img1)
inky_display.show()
print('Displaying temperature data')
img1.close()

time.sleep(90)

img2 = Image.new(
    'P', (inky_display.WIDTH, inky_display.HEIGHT), inky_display.BLACK)

display.windvane(img2)

inky_display.set_image(img2)
inky_display.show()
print('Displaying wind data')
img2.close()

time.sleep(90)

img3 = Image.new(
    'P', (inky_display.WIDTH, inky_display.HEIGHT), inky_display.BLACK)

display.celestial_info(img3)

inky_display.set_image(img3)
inky_display.show
print("Displaying celestial data")
img3.close
