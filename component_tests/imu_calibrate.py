import time
import board
import adafruit_mpu6050
import csv
#calculate offsets for IMU1, for calibration
#NOTE: Assumes z axis is perfectly vertical and subtracts the acceleration due to gravity, g=9.80665 m/s^2

G = 9.80665 #m/s^2

IMU_x_adj = 0
IMU_y_adj = 0
IMU_z_adj = 0

SWS_x_adj = 0
SWS_y_adj = 0
SWS_z_adj = 0

x_a_offset = 0
y_a_offset = 0
z_a_offset = 0

i2c = board.I2C()	#initialize the i2c interface
imu = adafruit_mpu6050.MPU6050(i2c, 0x69)	#initialize the mpu object
sws = adafruit_mpu6050.MPU6050(i2c, 0x68)	#initialize the mpu object

print("Starting IMU Calibration...")

for i in range(12000):  #2-minute calibration run.

    a_x,a_y,a_z=imu.acceleration

    a_x= a_x - IMU_x_adj
    a_y= a_y - IMU_y_adj
    a_z= a_z - IMU_z_adj

    x_a_offset = x_a_offset + (a_x-x_a_offset)/(i+1) # Coninually-updated average formula
    y_a_offset = y_a_offset + (a_y-y_a_offset)/(i+1)
    z_a_offset = z_a_offset + (a_z-z_a_offset)/(i+1)

	#print(imu.acceleration[0],",",imu.acceleration[1],",",imu.acceleration[2])
	#print(imu.gyro[0],",",imu.gyro[1],",",imu.gyro[2])
    time.sleep(0.01)

print("IMU accel. offset values:\tX=",x_a_offset,"\tY=",y_a_offset,"\tZ=",z_a_offset-G)

x_a_offset = 0
y_a_offset = 0
z_a_offset = 0

time.sleep(1)
print("Starting SWS Calibration")

for i in range(12000):  #2-minute calibration run.

    a_x,a_y,a_z=sws.acceleration

    a_x= a_x - SWS_x_adj
    a_y= a_y - SWS_y_adj
    a_z= a_z - SWS_z_adj

    x_a_offset = x_a_offset + (a_x-x_a_offset)/(i+1) # Coninually-updated average formula
    y_a_offset = y_a_offset + (a_y-y_a_offset)/(i+1)
    z_a_offset = z_a_offset + (a_z-z_a_offset)/(i+1)

    time.sleep(0.01)

print("SWS accel. offset values:\tX=",x_a_offset,"\tY=",y_a_offset,"\tZ=",z_a_offset-G)
