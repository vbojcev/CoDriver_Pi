import time
import board
import adafruit_mpu6050


#calculate offsets for IMU1, for calibration

IMU_x_adj = 0.5029609161732991
IMU_y_adj = 0.22429359992675774
IMU_z_adj = -1.592849395909651

SWS_x_adj = 0.3495626201558422
SWS_y_adj = 0.0903922856119797
SWS_z_adj = -0.16447526951499292

i2c = board.I2C()	#initialize the i2c interface
imu = adafruit_mpu6050.MPU6050(i2c, 0x69)	#initialize the imu object
sws = adafruit_mpu6050.MPU6050(i2c, 0x68)	#initialize the sws object

while True:
	a_x,a_y,a_z=sws.acceleration
	print(a_x-SWS_x_adj,",\t",a_y-SWS_y_adj,",\t",a_z-SWS_z_adj)
	time.sleep(0.01)	#print every 10ms
