#7/11/2022: NOT YET TESTED.

import obd
import time

carPort = obd.ODB()

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