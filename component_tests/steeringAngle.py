import board
import time

import numpy as np
import statistics as stat
from collections import deque


class SWS_Manager:

    def __init__(self, i2cBus):
        #init interface
        self.hwInterface = MPU.MPU6050(i2cBus, 0x68)
        #Calibrated offsets for the SWS (x,y,z).
        self.ADJ = (0.3495626201558422,0.0903922856119797,-0.16447526951499292)
        self.kalmanFilter_accel = [deque([0,0,0,0,0]),deque([0,0,0,0,0]),deque([0,0,0,0,0])]
        self.accel = (0,0,0)
        self.angle = 0

    def update(self):
        accelRaw = np.subtract(self.hwInterface.acceleration, self.ADJ)
        self.kalmanFilter_accel[0].popleft()
        self.kalmanFilter_accel[0].append(accelRaw[0])
        self.kalmanFilter_accel[1].popleft()
        self.kalmanFilter_accel[1].append(accelRaw[1])
        self.kalmanFilter_accel[2].popleft()
        self.kalmanFilter_accel[2].append(accelRaw[2])
        self.accel = (stat.fmean(self.kalmanFilter_accel[0]),stat.fmean(self.kalmanFilter_accel[1]),stat.fmean(self.kalmanFilter_accel[2]),)

    def read(self):
        return self.angle  

if __name__ == "__main__":
    i2c = board.I2C()
    sws=SWS_Manager(i2c)
    print()
    time.sleep(0.1)
    pass