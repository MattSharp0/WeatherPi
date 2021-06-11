from PIL import Image, ImageDraw, ImageFont
from weather_data import get_weather

width = 250
height = 122
img = Image.new(mode='RGB', size=(width, height), color=(0, 0, 0))
draw = ImageDraw.Draw(im=img, mode='RGB')


def windvane():
    # get wind data
    conditions = get_weather()
    windspd = conditions['windSpeed']
    windgust = conditions['windGust']
    winddir = conditions['windDir']
    pressure = conditions['pressure']
    day = conditions['day']
    date = conditions['date']

    print(winddir, windspd, windgust)
    wind = f"{day}, {date}\n \nWind Speed: {windspd}mph \nGusting: {windgust}mph \nPressure: {pressure}in"

    draw.text(xy=(24, 24), text=wind)

    # correct for draw start angle ()
    winddir -= 90

    # def screen areas
    screenright = [(149, 24), (225, 100)]

    # cardinal direction lines
    draw.line(xy=[(187, 20), (187, 104)], fill=(255, 255, 255,), width=1)
    draw.line(xy=[(145, 62), (229, 62)], fill=(255, 255, 255,), width=1)

    # Direction indicators
    # font = ImageFont.load()
    draw.text(xy=(185, 7), text='N', fill=(255, 255, 0))
    draw.text(xy=(185, 105), text='S', fill=(255, 255, 255))
    draw.text(xy=(235, 57), text='E', fill=(255, 255, 255))
    draw.text(xy=(135, 57), text='W', fill=(255, 255, 255))

    # compass perimeter
    draw.arc(xy=screenright, start=(winddir + 15),
             end=(winddir - 15), fill=(255, 255, 255))

    # wind direction
    draw.pieslice(xy=screenright, start=(winddir - 15), end=(winddir + 15),
                  fill=(255, 255, 0), outline=(255, 255, 0))
    """
    Overlays wind direction onto a compass rose displayed on right half of screen
    """


windvane()

img.show()
img.close()
