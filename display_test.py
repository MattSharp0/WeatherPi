from PIL import Image, ImageDraw
from weather_data import get_conditions

width = 250
height = 122
xy = [(50, 30), (200, 90)]

img = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))

draw = ImageDraw.Draw(im=img, mode='RGB')

# draw.line(xy=xy, fill=(0, 0, 0), width=2)


windDir = get_conditions()['windDir']
print(windDir)


img.show()
# img.save('testimg.png')
img.close()
