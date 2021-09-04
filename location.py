from gps import *


class Location:
    def __init__(self):
        self.gpsd = gps(mode=WATCH_ENABLE | WATCH_NEWSTYLE)

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
