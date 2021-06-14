from PIL import ImageFont, ImageDraw
from weather_data import get_weather
from font_fredoka_one import FredokaOne

# allows for testing without inky library
try:
    from inky.auto import auto
    inky_display = auto()
    black = inky_display.BLACK
    white = inky_display.WHITE
    yellow = inky_display.YELLOW
except ImportError:
    black = (0, 0, 0)
    white = (255, 255, 255)
    yellow = (255, 255, 0)

# set up fonts
font = ImageFont.truetype(FredokaOne, 16)
font_sm = ImageFont.truetype(FredokaOne, 14)


def draw_windvane(img, nightmode):
    """
    Takes params 'draw' (DrawImage obj) and 'nightmode' (boolean). Prints wind test data on left side of img and a compass with wind direction on right side.
    """
    # changes colors if nightmode is True
    if nightmode:
        try:
            black = inky_display.WHITE
        except:
            black = (255, 255, 255)
    else:
        try:
            black = inky_display.BLACK
        except:
            black = (0, 0, 0)

    # Create canvass
    draw = ImageDraw.Draw(im=img)

    # get wind data
    conditions = get_weather()
    windspd = conditions['windSpeed']
    windgust = conditions['windGust']
    winddir = conditions['windDir']
    pressure = conditions['pressure']
    day = conditions['day']
    date = conditions['date']

    # Wind text
    wind = f"{day}, {date}\n~~Wind~~\nSpeed: {windspd}mph \nGusting: {windgust}mph \nPressure: {pressure}in"

    # draw text
    draw.text(xy=(14, 10), text=wind, fill=black, font=font)

    # correct for draw default start angle at 90deg
    winddir -= 90

    # def screen area
    screenright = [(149, 24), (225, 100)]

    # cardinal direction lines
    draw.line(xy=[(187, 20), (187, 104)], fill=black, width=1)
    draw.line(xy=[(145, 62), (229, 62)], fill=black, width=1)

    # Cardinal directions
    draw.text(xy=(182, 3), text='N', fill=yellow, font=font)
    draw.text(xy=(183, 103), text='S', fill=black, font=font_sm)
    draw.text(xy=(231, 54), text='E', fill=black, font=font_sm)
    draw.text(xy=(131, 54), text='W', fill=black, font=font_sm)

    # compass perimeter
    draw.arc(xy=screenright, start=(winddir + 15),
             end=(winddir - 15), fill=black, width=3)

    # wind direction
    draw.pieslice(xy=screenright, start=(winddir - 15), end=(winddir + 15),
                  fill=yellow, outline=yellow)


def draw_temperature(img, nightmode):
    '''
    Takes params 'draw' (DrawImage obj) and 'nightmode' (boolean). Prints temp data on left side of img and weather icon on the right.
    '''

    # changes colors if nightmode is True
    if nightmode:
        try:
            black = inky_display.WHITE
        except:
            black = (255, 255, 255)
    else:
        try:
            black = inky_display.BLACK
        except:
            black = (0, 0, 0)

    # Create canvass
    draw = ImageDraw.Draw(im=img)

    # get the weather
    conditions = get_weather()
    day = conditions['day']
    date = conditions['date']
    temp = conditions['temp']
    high = conditions['high']
    low = conditions['low']
    uv = int(conditions['uv'])
    humidity = conditions['humidity']

    # degrees F symbol
    degf = u'\N{DEGREE SIGN}' + 'F'

    # change None to -
    if high == None:
        high = '--'

    if low == None:
        low = '--'
    # create temp text
    temptext = f'{day}, {date}\nTemp:  {temp}{degf}\nH/L:  {high}{degf} | {low}{degf}\nUV Index:  {uv}\nHumidity: {humidity}%'

    # draw text
    draw.text(xy=(14, 10), text=temptext, fill=black, font=font)


def draw_celestial_info(img, nightmode):
    '''
    '''
    pass


def draw_outlook(img, nightmode):
    '''
    '''
    pass
