import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import time

import serial

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

SERIAL_PORT = "/dev/serial0"


def formatDegreesMinutes(coordinates, digits):

    parts = coordinates.split(".")

    if (len(parts) != 2):
        return coordinates

    if (digits > 3 or digits < 2):
        return coordinates

    left = parts[0]
    right = parts[1]
    degrees = str(left[:digits])
    minutes = str(right[:3])

    return degrees + "." + minutes


def getPositionData(gps):
    data = gps.readline()
    while True:
        message = data[0:6]
        if (message == "$GPRMC"):
            # GPRMC = Recommended minimum specific GPS/Transit data
            # Reading the GPS fix data is an alternative approach that also works
            parts = data.split(",")
            if parts[2] == 'V':
                # V = Warning, most likely, there are no satellites in view...
                return ("syncing", "syncing")
            else:
                # Get the position data that was transmitted with the GPRMC message
                # In this example, I'm only interested in the longitude and latitude
                # for other values, that can be read, refer to: http://aprs.gids.nl/nmea/#rmc
                longitude = formatDegreesMinutes(parts[5], 3)
                latitude = formatDegreesMinutes(parts[3], 2)
                return (str(latitude), str(longitude))
        else:
            # Handle other NMEA messages and unsupported strings
            pass


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

gps = serial.Serial(SERIAL_PORT, baudrate=9600, timeout=0.5)

while True:
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    lat, lon = getPositionData(gps)
    draw.text((x, top), f"la:{lat}",  font=font, fill=255)
    draw.text((x, top+8), f"lo:{lon}", font=font, fill=255)
    draw.text((x, top+16), "little",  font=font, fill=255)
    draw.text((x, top+25), "baka",  font=font, fill=255)

    disp.image(image)
    disp.display()
    time.sleep(.5)
