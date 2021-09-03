# system setup
sudo raspi-config nonint do_hostname gormin

# gps dependencies
sudo apt-get install gpsd gpsd-clients

# gps settings
sudo raspi-config nonint do_serial 1

# screen dependencies
sudo apt install -y python3-dev
sudo apt install -y python-smbus i2c-tools
sudo apt install -y python3-pil
sudo apt install -y python3-pip
sudo apt install -y python3-setuptools
sudo apt install -y python3-rpi.gpio

# screen settings
sudo raspi-config nonint do_i2c 1