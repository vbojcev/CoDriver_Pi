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

imu_kalmanFilter = [deque([0,0,0,0,0]),deque([0,0,0,0,0]),deque([0,0,0,0,0])]
sws_kalmanFilter = [deque([0,0,0,0,0]),deque([0,0,0,0,0]),deque([0,0,0,0,0])]

i2c = board.I2C()	#initialize the i2c interface
imu = adafruit_mpu6050.MPU6050(i2c, 0x69)	#initialize the imu object
sws = adafruit_mpu6050.MPU6050(i2c, 0x68)	#initialize the sws object

numSampled = 0

initTime = time.time()

def updateFilter(raw, filter):
	filter[0].popleft()
	filter[0].append(raw[0])
	filter[1].popleft()
	filter[1].append(raw[1])
	filter[2].popleft()
	filter[2].append(raw[2])

for i in range(10000):
	sws_accelRaw = np.subtract(sws.acceleration, SWS_ADJ)
	imu_accelRaw = np.subtract(imu.acceleration, IMU_ADJ)
	updateFilter(sws_accelRaw, sws_kalmanFilter)
	sws_accel=(stat.fmean(sws_kalmanFilter[0]),stat.fmean(sws_kalmanFilter[1]),stat.fmean(sws_kalmanFilter[2]),)
	print("%.2f\t%.2f\t%.2f\tm/s^2" % (sws_accel))

print("Total time elapsed is ",time.time() - initTime,".")
