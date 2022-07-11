import time
import board
import adafruit_mpu6050
import csv

#7/4/2022: NOT YET TESTED

#calculate offsets for IMU1, for calibration
#NOTE: Assumes z axis is perfectly vertical and subtracts the acceleration due to gravity, g=9.80665 m/s^2

G = 9.80665

x_a_offset = 0
y_a_offset = 0
z_a_offset = 0

i2c = board.I2C()	#initialize the i2c interface
imu = adafruit_mpu6050.MPU6050(i2c)	#initialize the mpu object

for i in range(10000):  #100 seconds calibration run.

    a_x,a_y,a_z=imu.acceleration

    x_a_offset = x_a_offset + (a_x-x_a_offset)/(i+1) # Coninually-updated average formula
    y_a_offset = y_a_offset + (a_y-y_a_offset)/(i+1)
    z_a_offset = z_a_offset + (a_z-z_a_offset)/(i+1)

	#print(imu.acceleration[0],",",imu.acceleration[1],",",imu.acceleration[2])
	#print(imu.gyro[0],",",imu.gyro[1],",",imu.gyro[2])
    time.sleep(0.01)

print("Final offset values:\tX=",x_a_offset,"\tY=",y_a_offset,"\tZ=",z_a_offset-G)