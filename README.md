# CoDriver_Pi
The code that runs on CoDriver's microcontroller. CoDriver uses Python and Adafruit's circuitpython libraries to interface with sensors.

component_tests contains python scripts to test the IMU/SWS, GPS, etc.

Upon a fresh install of PiOS, there are several steps to complete before running any code.

https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi

1. sudo apt-get update
2. sudo apt-get upgrade
3. sudo pip3 install --upgrade adafruit-python-shell    #Basic Board Access (GPIO, I2C, SPI)
4. sudo pip3 install adafruit-circuitpython-mpu6050     #IMU and SWS access
5. sudo pip3 install adafruit-circuitpython-gps         #GPS access
6. sudo pip3 install adafruit-circuitpython-mcp3xxx     #ADC access for TPS,BPS,HRS