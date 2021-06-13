'''
Run this code on Pi ONLY. 
INKY library cannot be installed on other OS. 
'''

from PIL import Image
import display
from inky import InkyPHAT

inky_display = InkyPHAT("yellow")
inky_display.set_border(inky_display.WHITE)
img = Image.new('P', (inky_display.WIDTH, inky_display.HEIGHT))
