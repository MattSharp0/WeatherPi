import display
from PIL import Image

# define image (pHat display size)
width = 250
height = 122
img = Image.new(mode='RGB', size=(width, height), color=(0, 0, 0))

display.windvane(img)

img.show()
img.close()
