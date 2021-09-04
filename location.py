from gps import *
import os


class Location:
    def __init__(self):
        self.gpsd = gps(mode=WATCH_ENABLE | WATCH_NEWSTYLE)
        self.repair_socket()

    def repair_socket(self):
        os.system("sudo systemctl stop gpsd.socket")
        os.system("sudo gpsd /dev/serial0 -F /var/run/gpsd.sock")

    def get_latitude_longitude(self):
        while (True):
            position_data = self.get_positional_data()
            if (position_data != None):
                return position_data

    def get_positional_data(self):
        data = self.gpsd.next()
        if data['class'] == 'TPV':
            latitude = getattr(data, 'lat', "Unknown")
            longitude = getattr(data, 'lon', "Unknown")
            return (str(latitude), str(longitude))
        return None
