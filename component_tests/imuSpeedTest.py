import time
import board
import adafruit_mpu6050
import numpy as np
import statistics as stat
from collections import deque


#calculate offsets for IMU1, for calibration

IMU_x_adj = 0.5029609161732991
IMU_y_adj = 0.22429359992675774
IMU_z_adj = -1.592849395909651

IMU_ADJ = (IMU_x_adj,IMU_y_adj,IMU_z_adj)

SWS_x_adj = 0.3495626201558422
SWS_y_adj = 0.0903922856119797
SWS_z_adj = -0.16447526951499292

SWS_ADJ = (SWS_x_adj,SWS_y_adj,SWS_z_adj)

kalmanFilter = [deque([0,0,0,0,0]),deque([0,0,0,0,0]),deque([0,0,0,0,0])]

i2c = board.I2C()	#initialize the i2c interface
imu = adafruit_mpu6050.MPU6050(i2c, 0x69)	#initialize the imu object
sws = adafruit_mpu6050.MPU6050(i2c, 0x68)	#initialize the sws object

numSampled = 0

initTime = time.time()

for i in range(10000):
	accelRaw = np.subtract(sws.acceleration, SWS_ADJ)
	kalmanFilter[0].popleft()
	kalmanFilter[0].append(accelRaw[0])
	kalmanFilter[1].popleft()
	kalmanFilter[1].append(accelRaw[1])
	kalmanFilter[2].popleft()
	kalmanFilter[2].append(accelRaw[2])
	accel=(stat.fmean(kalmanFilter[0]),stat.fmean(kalmanFilter[1]),stat.fmean(kalmanFilter[2]),)

print("Total time elapsed is ",time.time() - initTime,".")
