'''
Run this code on Pi 
'''

from PIL import Image
import display
from inky.auto import auto

inky_display = auto()

img = Image.new('P', (inky_display.WIDTH, inky_display.HEIGHT),
                color=inky_display.WHITE)

display.windvane(img=img, nightmode=True)
inky_display.set_image(img)
inky_display.show()
