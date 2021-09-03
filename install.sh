# system setup
raspi-config nonint do_hostname gormin

# gps dependencies
apt-get install gpsd gpsd-clients

# gps settings
raspi-config nonint do_serial 1

# screen dependencies
apt install -y python3-dev
apt install -y python-smbus i2c-tools
apt install -y python3-pil
apt install -y python3-pip
apt install -y python3-setuptools
apt install -y python3-rpi.gpio

# screen settings
raspi-config nonint do_i2c 1