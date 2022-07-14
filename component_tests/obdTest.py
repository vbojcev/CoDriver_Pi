#7/11/2022: NOT YET TESTED.
#7/13/2022: CONNECTS TO ADAPTER, BUT NOT VEHICLE:
    """pi@CoDriver:~/CoDriver_Pi/component_tests $ python3 obdTest.py
    [obd.elm327] Failed to retrieve current protocol
    [obd.elm327] Adapter connected, but the ignition is off
    [obd.obd] Cannot load commands: No connection to car
    Traceback (most recent call last):
    File "/home/pi/CoDriver_Pi/component_tests/obdTest.py", line 15, in <module>
        speed = carPort.query(speedCMD).value.magnitude         #in kph
    AttributeError: 'NoneType' object has no attribute 'magnitude'"""
#TODO: Try fast=False, timeout=30, protocol=<1toA>
#TODO: Try older version 0.6.1 (https://stackoverflow.com/questions/60606277/problem-connecting-and-querying-a-car-with-python-obd). Guide to do this: https://stackoverflow.com/questions/5226311/installing-specific-package-version-with-pip
#TODO: Then try manually installing from github. Guide: https://www.activestate.com/resources/quick-reads/how-to-manually-install-python-packages/


import obd
import time

carPort = obd.OBD(fast=False, timeout=30)

#setup desired command names
speedCMD = obd.commands.SPEED
fuelCMD = obd.commands.FUEL_RATE
rpmCMD = obd.commands.RPM
throttleCMD = obd.commands.ACCELERATOR_POS_D

while True:
    speed = carPort.query(speedCMD).value.magnitude         #in kph
    fuel_rate = carPort.query(fuelCMD).value.magnitude      #in l/h
    engineRPM = carPort.query(rpmCMD).value.magnitude       #in RPM
    accelPedal = carPort.query(throttleCMD).value.magnitude #in %
    #print("Speed:\t",speed,"\tFuel:\t",fuel_rate,"\tRPM:\t",engineRPM,"Throttle:\t",accelPedal)
    #time.sleep(0.2)
    print(time.time(),",",speed,",",fuel_rate,",",engineRPM,",",accelPedal)
    time.sleep(0.01)