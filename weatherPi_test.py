'''
Locally executable program to test weatherPi functions without Inky libraries.
Shows images as temp .png file.
'''

import display
from PIL import Image

# define image for local test (pHat display size = 250x122)
width = 250
height = 122

# set to true for black background
nightmode = True

if nightmode:
    color = (0, 0, 0)
else:
    color = (240, 240, 240)

img = Image.new(mode='RGB', size=(width, height), color=color))
display.windvane(img, nightmode)

img.show()
img.close()
