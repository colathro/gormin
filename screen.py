import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class Screen:
    padding = -2
    top = padding

    def __init__(self):
        self.RST = None

        self.disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
        disp.begin()
        disp.clear()
        disp.display()

        self.image = Image.new('1', (disp.width, disp.height))
        self.draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, width, height), outline=0, fill=0)

        self.font = ImageFont.load_default()

    def render(self, line1, line2, line3, line4):
        self.draw.rectangle((0, 0, width, height), outline=0, fill=0)

        self.draw.text((x, top), line1,  font=font, fill=255)
        self.draw.text((x, top+8), line2, font=font, fill=255)
        self.draw.text((x, top+16), line3,  font=font, fill=255)
        self.draw.text((x, top+25), line4,  font=font, fill=255)

        self.disp.image(image)
        self.disp.display()
