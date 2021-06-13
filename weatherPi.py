'''
Run this code on Pi ONLY. 
INKY library cannot be installed on other OS. 
'''

from PIL import Image
import display
from inky.auto import auto

inky_display = auto()

img = Image.new('P', (inky_display.WIDTH, inky_display.HEIGHT))

display.windvane(img=img)
inky_display.set_image(img)
inky_display.show()
