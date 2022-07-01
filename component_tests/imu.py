import time
import board
import adafruit_mpu6050


#calculate offsets for IMU1, for calibration

if 0:
	#IMU1 accel. calibration
	X_A_OFFSET = 0.514183
	Y_A_OFFSET = 0.287291
	Z_A_OFFSET = -1.59902
	#IMU1 gyro calibration(TODO)
	X_G_OFFSET = 0
	Y_G_OFFSET = 0
	Z_G_OFFSET = 0
else:
	#IMU2 accel. calibration (TODO)
	X_A_OFFSET = 0.465351637
	Y_A_OFFSET = 0.141331404
	Z_A_OFFSET = -0.194544327
	#IMU2 gyro calibration (TODO)
	X_G_OFFSET = 0
	Y_G_OFFSET = 0
	Z_G_OFFSET = 0

i2c = board.I2C()	#initialize the i2c interface
imu = adafruit_mpu6050.MPU6050(i2c)	#initialize the mpu object

while True:
	#calibration was done by printing in comma delineation, finding average offest in Excel
	print(imu.acceleration[0]-X_A_OFFSET,",",imu.acceleration[1]-Y_A_OFFSET,",",imu.acceleration[2]-Z_A_OFFSET)
	#print("%.5f,%.5f,%.5f" % (imu.gyro))	#test gyroscope
	#print("Temperature: %.2f C" % mpu.temperature)	#test temperature
	time.sleep(0.01)	#print every 10ms
