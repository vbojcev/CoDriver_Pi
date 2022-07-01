import time
import board
import adafruit_mpu6050

X_A_OFFSET = 0.514183
Y_A_OFFSET = 0.287291
Z_A_OFFSET = -1.59902

i2c = board.I2C()
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
	print(mpu.acceleration[0]-X_A_OFFSET,",",mpu.acceleration[1]-Y_A_OFFSET,",",mpu.acceleration[2]-Z_A_OFFSET)
	#print("%.5f,%.5f,%.5f" % (mpu.gyro))
	#print("Temperature: %.2f C" % mpu.temperature)
	#print("")
	time.sleep(0.01)
