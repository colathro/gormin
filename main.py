from location import Location
from screen import Screen

import time
import datetime

if __name__ == "__main__":
    s = Screen()
    l = Location()

    while True:
        data = l.get_latitude_longitude()
        s.render("Gormin G420", "la:" + data[0], "lon:" + data[1], "Running")
        with open("data.csv", "a") as f:
            f.write(f"{datetime.datetime.now()},{data[0]},{data[1]}\n\r")
        time.sleep(1)
