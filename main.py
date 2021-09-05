from location import Location
from screen import Screen

import time
import datetime
import threading
from gpiozero import Button


class State:

    def __init__(self):
        self.running = True
        self.data = ("Unknown", "Unknown")
        self.button = Button(17)
        thread = threading.Thread(target=self.await_pause, args=())
        thread.daemon = True
        thread.start()

    def await_pause(self):
        while True:
            self.button.wait_for_press()
            print("ye")
            # self.running = not self.running
            time.sleep(.5)


if __name__ == "__main__":
    s = Screen()
    l = Location()
    state = State()

    while True:
        if state.running:
            state.data = l.get_latitude_longitude()
            s.render("Gormin 420", "la:" +
                     state.data[0], "lon:" + state.data[1], "Running")
            with open("data.csv", "a") as f:
                f.write(
                    f"{datetime.datetime.now()},{state.data[0]},{state.data[1]}\n\r")
        else:
            s.render("Gormin 420", "la:" +
                     state.data[0], "lon:" + state.data[1], "Stopped")
        time.sleep(1)
