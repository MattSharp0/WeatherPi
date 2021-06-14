'''
Locally executable program to test weatherPi functions without Inky libraries.
Shows images as temp .png file.
'''

from PIL import Image
import display

# define image for local test (pHat display size = 250x122)
width = 250
height = 122

# set to true for black background
nightmode = True

if nightmode:
    color = (0, 0, 0)
else:
    color = (240, 240, 240)

windvane = Image.new(mode='RGB', size=(width, height), color=color)
temperature = Image.new(mode='RGB', size=(width, height), color=color)

display.draw_windvane(windvane, nightmode)

display.draw_temperature(temperature, nightmode)

windvane.show()
temperature.show()

windvane.close()
temperature.close()
