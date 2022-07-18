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
7. sudo apt-get install bluetooth bluez blueman   #Bluetooth utilities
8. sudo bluetoothctl    #open bluetooth manager
9. agent on
10. discoverable on
11. scan on             
12. trust "device MAC address (00:1D:A5:01:6E:17 for current adapter)" #only once the desired deice shows up on the scan
13. pair "device MAC address"
14. sudo pip3 install obd
15. sudo nano /etc/rc.local >> add the line "sudo rfcomm bind rfcomm1 00:1D:A5:01:6E:17" #This allows on-demand usage of the OBD2 when in range
16. sudo pip3 install threading
17. sudo pip3 install datetime
18. sudo pip3 install csv

