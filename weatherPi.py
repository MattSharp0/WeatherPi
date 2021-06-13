'''
Run this code on Pi 
'''

from PIL import Image
import display
from inky.auto import auto

inky_display = auto()

nightmode = True
if nightmode:
    base_color = inky_display.BLACK
else:
    base_color = inky_display.WHITE

img = Image.new('P', (inky_display.WIDTH, inky_display.HEIGHT),
                color=base_color)

display.windvane(img=img, nightmode=nightmode)
inky_display.set_image(img)
inky_display.show()
