import display
from PIL import Image

# comment out below code to run locally
# from inky import InkyPHAT
# inky_display = InkyPHAT("yellow")
# inky_display.set_border(inky_display.WHITE)
# img = Image.new('P', (inky_display.WIDTH, inky_display.HEIGHT))

# define image for local test (pHat display size = 250x122)
width = 250
height = 122
img = Image.new(mode='RGB', size=(width, height), color=(0, 0, 0))

display.windvane(img)

img.show()
img.close()
