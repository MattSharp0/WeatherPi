'''
Locally executable program to test weatherPi functions without Inky libraries.
Shows images as temp .png file.
'''

import display
from PIL import Image

# define image for local test (pHat display size = 250x122)
width = 250
height = 122
img = Image.new(mode='RGB', size=(width, height), color=(240, 240, 240))

display.windvane(img)

img.show()
img.close()
