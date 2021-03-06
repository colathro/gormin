#!/bin/bash

# system setup
sudo raspi-config nonint do_hostname gormin

# gps dependencies
sudo apt-get install gpsd gpsd-clients

# gps settings
sudo raspi-config nonint do_serial 0

# screen dependencies
sudo apt install -y python3-dev
sudo apt install -y python-smbus i2c-tools
sudo apt install -y python3-pil
sudo apt install -y python3-pip
sudo apt install -y python3-setuptools
sudo apt install -y python3-rpi.gpio

# screen settings
sudo raspi-config nonint do_i2c 0

# python dependencies
sudo pip3 install Adafruit-SSD1306
sudo pip3 install pyserial

# setup rc.local
sudo mv rc.local /etc/rc.local
echo moving rc.local to /etc/rc.local
