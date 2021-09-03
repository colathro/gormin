import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import time
from gps import *

import serial

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def getPositionData(gps):
    nx = gpsd.next()
    # For a list of all supported classes and fields refer to:
    # https://gpsd.gitlab.io/gpsd/gpsd_json.html
    if nx['class'] == 'TPV':
        latitude = getattr(nx, 'lat', "Unknown")
        longitude = getattr(nx, 'lon', "Unknown")
        return (str(longitude), str(latitude))
    return ("passing", "passing")


RST = None
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)

draw.rectangle((0, 0, width, height), outline=0, fill=0)

padding = -2
top = padding
bottom = height-padding

x = 0

font = ImageFont.load_default()

gpsd = gps(mode=WATCH_ENABLE | WATCH_NEWSTYLE)

while True:
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    lat, lon = getPositionData(gpsd)
    draw.text((x, top), f"la:{lat}",  font=font, fill=255)
    draw.text((x, top+8), f"lo:{lon}", font=font, fill=255)
    draw.text((x, top+16), "little",  font=font, fill=255)
    draw.text((x, top+25), "baka",  font=font, fill=255)

    disp.image(image)
    disp.display()
    time.sleep(.5)
