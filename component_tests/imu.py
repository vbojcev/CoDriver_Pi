import time
import board
import adafruit_mpu6050
import numpy as np


#calculate offsets for IMU1, for calibration

IMU_x_adj = 0.5029609161732991
IMU_y_adj = 0.22429359992675774
IMU_z_adj = -1.592849395909651

IMU_ADJ = (IMU_x_adj,IMU_y_adj,IMU_z_adj)

SWS_x_adj = 0.3495626201558422
SWS_y_adj = 0.0903922856119797
SWS_z_adj = -0.16447526951499292

SWS_ADJ = (SWS_x_adj,SWS_y_adj,SWS_z_adj)

i2c = board.I2C()	#initialize the i2c interface
imu = adafruit_mpu6050.MPU6050(i2c, 0x69)	#initialize the imu object
sws = adafruit_mpu6050.MPU6050(i2c, 0x68)	#initialize the sws object

while True:
	accel = tuple(np.subtract(sws.acceleration, SWS_ADJ))
	print("X:%.2f,\tY: %.2f,\tZ: %.2f\tm/s^2" % (accel))
	time.sleep(0.01)	#print every 10ms
