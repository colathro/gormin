from location import Location
from screen import Screen

if __name__ == "__main__":
    s = Screen()
    l = Location()

    while True:
        data = l.get_latitude_longitude()
        s.render("Gormin G420", "la:" + data[0], "lon:" + data[1], "Running")
