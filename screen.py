import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class Screen:
    padding = -2
    top = padding

    def __init__(self):
        self.disp = Adafruit_SSD1306.SSD1306_128_32(rst=None)
        self.disp.begin()
        self.disp.clear()
        self.disp.display()

        self.image = Image.new('1', (self.disp.width, self.disp.height))
        self.draw = ImageDraw.Draw(self.image)
        self.draw.rectangle(
            (0, 0, self.disp.width, self.disp.height), outline=0, fill=0)

        self.font = ImageFont.load_default()

    def render(self, line1, line2, line3, line4):
        self.draw.rectangle(
            (0, 0, self.disp.width, self.disp.height), outline=0, fill=0)

        self.draw.text((0, self.top), line1,  font=font, fill=255)
        self.draw.text((0, self.top+8), line2, font=font, fill=255)
        self.draw.text((0, self.top+16), line3,  font=font, fill=255)
        self.draw.text((0, self.top+25), line4,  font=font, fill=255)

        self.disp.image(self.image)
        self.disp.display()
