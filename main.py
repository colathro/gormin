from location import Location
from screen import Screen

import time
import datetime
import threading
from gpiozero import Button


class State:

    def __init__(self):
        self.running = False
        self.button = Button(17)
        thread = threading.Thread(target=self.await_pause, args=())
        thread.daemon = True
        thread.start()

    def await_pause(self):
        while True:
            self.button.wait_for_press()
            self.running = not self.running


if __name__ == "__main__":
    s = Screen()
    l = Location()
    state = State()

    while True:
        if state.running:
            data = l.get_latitude_longitude()
            s.render("Gormin 420", "la:" +
                     data[0], "lon:" + data[1], "Running")
            with open("data.csv", "a") as f:
                f.write(f"{datetime.datetime.now()},{data[0]},{data[1]}\n\r")
        else:
            s.render("Gormin 420", "la:" +
                     data[0], "lon:" + data[1], "Stopped")
        time.sleep(1)
