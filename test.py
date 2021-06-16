'''
Locally executable program to test weatherPi functions without Inky libraries.
Shows images as temp .png file.
'''

from PIL import Image
import display

# define image for local test (pHat display size = 250x122)
width = 250
height = 122

img1 = Image.new(mode='RGB', size=(width, height), color=(0, 0, 0))
img2 = Image.new(mode='RGB', size=(width, height), color=(0, 0, 0))
img3 = Image.new(mode='RGB', size=(width, height), color=(0, 0, 0))

display.temperature(img1)
img1.show()
img1.close()

display.windvane(img2)
img2.show()
img2.close()

display.celestial_info(img3)
img3.show()
img3.close()
