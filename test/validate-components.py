import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

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

while True:
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    disp.image(image)
    draw.text((x, top), "you are",  font=font, fill=255)
    draw.text((x, top+8), "a sussy", font=font, fill=255)
    draw.text((x, top+16), "little",  font=font, fill=255)
    draw.text((x, top+25), "baka",  font=font, fill=255)
    disp.display()
    time.sleep(.5)
