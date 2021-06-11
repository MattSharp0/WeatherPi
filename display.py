from PIL import ImageDraw
from weather_data import get_weather


def windvane(img):
    """
    Draws wind data onto supplied PIL 'img' object. Left side shows text data, right side shows direction on compass rose
    """
    # create image draw object
    draw = ImageDraw.Draw(im=img, mode='RGB')

    # get wind data
    conditions = get_weather()
    windspd = conditions['windSpeed']
    windgust = conditions['windGust']
    winddir = conditions['windDir']
    pressure = conditions['pressure']
    day = conditions['day']
    date = conditions['date']

    # Wind text
    wind = f"{day}, {date}\n \nWind Speed: {windspd}mph \nGusting: {windgust}mph \nPressure: {pressure}in"
    draw.text(xy=(24, 24), text=wind)

    # correct for draw start angle ()
    winddir -= 90

    # def screen area
    screenright = [(149, 24), (225, 100)]

    # cardinal direction lines
    draw.line(xy=[(187, 20), (187, 104)], fill=(255, 255, 255,), width=1)
    draw.line(xy=[(145, 62), (229, 62)], fill=(255, 255, 255,), width=1)

    # Cardinal directions
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


def weather(img):
    '''
    '''

    # create image draw object
    draw = ImageDraw.Draw(im=img, mode='RGB')

    # get weather
    conditions = get_weather()


def moonphases(img):
    '''
    '''
    pass
