#IMPORTS
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#Basics
import time
import datetime
import threading
import numpy as np
import statistics as stat
from collections import deque
import csv

#Hardware interfacing
import board
import busio
import digitalio as dio

#Sensor-specific
import obd
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import adafruit_gps as GPS
import adafruit_mpu6050 as MPU

#/////////////////////////////////////////////////////////

#GLOBAL CONSTANTS
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#Standard acceleration due to gravity
G = 9.807

#/////////////////////////////////////////////////////////

#GLOBAL VARIABLES
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#/////////////////////////////////////////////////////////

#FUNCTION DEFINITIONS
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#/////////////////////////////////////////////////////////

#CLASS DEFINITIONS
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

class DataManager:

    def __init__(self):
        #content=[time,lat,long,speed,fuel_rate,throttle,brake,steer_angle,fw_accel,sw_accel,fw_pitch_wre,sw_pitch_rate,heart_rate]
        #size=13
        self.content=[0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.numRows = 0
        self.fileIndex = 0
        self.currentFile = open('data0.csv', 'w', newline='')
        self.writer = csv.writer(self.currentFile)

    def record(self):   #UNTESTED
        self.updateTime(time.time())
        self.writer.writerow(self.content)
        self.numRows += 1
        if (self.numRows > 1000):   #Maximum file size reached
            self.currentFile.close()
            self.fileIndex += 1
            self.currentFile = open('data'+str(self.fileIndex)+'.csv', 'w', newLine='')
            self.writer = csv.writer(self.currentFile)
            self.numRows = 0

    def updateTime(self, timeStamp):
        self.content[0] = timeStamp

    def updateLoc(self, loc):
        self.content[1] = loc(0)
        self.content[2] = loc(1)

    def updateSpeed(self, speed):
        self.content[4] = speed

    def updateFuel(self, fuel):
        self.content[4] = fuel

    def updatePedals(self, pedals):
        self.content[5] = pedals[0]
        self.content[6] = pedals[1]

    def updateSteer(self, steer):
        self.content[7] = steer

    def updateAccel(self, accel):
        self.content[8] = accel[0]
        self.content[9] = accel[1]

    def updateAccel(self, accel):
        self.content[8] = accel[0]
        self.content[9] = accel[1]

    def updatePitch(self, pitch):
        self.content[8] = pitch[0]
        self.content[9] = pitch[1]


class IMU_Manager:

    def __init__(self, i2cBus):
        #init interface
        self.hwInterface = MPU.MPU6050(i2cBus, 0x69)
        #Calibrated offsets for the IMU (x,y,z).
        self.ADJ = (0.5029609161732991,0.22429359992675774,-1.592849395909651)
        self.kalmanFilter = [deque([0,0,0,0,0]),deque([0,0,0,0,0]),deque([0,0,0,0,0])]
        self.accel = (0,0,0)

    def update(self):
        accelRaw = np.subtract(self.hwInterface.acceleration, self.ADJ)
        self.kalmanFilter[0].popleft()
        self.kalmanFilter[0].append(accelRaw[0])
        self.kalmanFilter[1].popleft()
        self.kalmanFilter[1].append(accelRaw[1])
        self.kalmanFilter[2].popleft()
        self.kalmanFilter[2].append(accelRaw[2])
        self.accel = (stat.fmean(self.kalmanFilter[0]),stat.fmean(self.kalmanFilter[1]),stat.fmean(self.kalmanFilter[2]),)

    def read(self):
        return self.accel

class SWS_Manager:

    def __init__(self, i2cBus):
        #init interface
        self.hwInterface = MPU.MPU6050(i2cBus, 0x68)
        #Calibrated offsets for the SWS (x,y,z).
        self.ADJ = (0.3495626201558422,0.0903922856119797,-0.16447526951499292)
        self.kalmanFilter = [deque([0,0,0,0,0]),deque([0,0,0,0,0]),deque([0,0,0,0,0])]
        self.accel = (0,0,0)

    def update(self):
        accelRaw = np.subtract(self.hwInterface.acceleration, self.ADJ)
        self.kalmanFilter[0].popleft()
        self.kalmanFilter[0].append(accelRaw[0])
        self.kalmanFilter[1].popleft()
        self.kalmanFilter[1].append(accelRaw[1])
        self.kalmanFilter[2].popleft()
        self.kalmanFilter[2].append(accelRaw[2])
        self.accel = (stat.fmean(self.kalmanFilter[0]),stat.fmean(self.kalmanFilter[1]),stat.fmean(self.kalmanFilter[2]),)    

class GPS_Manager:

    def __init__(self, i2cBus):
        self.hwInterface = GPS.GPS_GtopI2C(i2cBus)

#/////////////////////////////////////////////////////////

#MAIN
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
if __name__ == '__main__':

    #Initialization
    #=====================================================

    #Hardware Serial Interfaces
    i2c = board.I2C()
    spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

    #Initialize GPS
    gps = GPS_Manager(i2c)

    #Initialize ADC
    cs = dio.DigitalInOut(board.D5)
    mcp = MCP.MCP3008(spi, cs)

    #Initialize analog sensors as channels in the ADC:
    hrs = AnalogIn(mcp, MCP.P0)
    tps = AnalogIn(mcp, MCP.P1)
    bps = AnalogIn(mcp, MCP.P2)

    #Initialize Motion Sensors
    imu = IMU_Manager(i2c)
    sws = SWS_Manager(i2c)

    #Initialize Data Manager
    data = DataManager()

    #Timing initialization
    initTime = time.monotonic_ns()
    #=====================================================

    #Main Loop
    while True:

        #Perform as often as possible, no timing specified
        #-------------------------------------------------
        #-------------------------------------------------

        #Perform every 10 milliseconds
        #-------------------------------------------------
        #-------------------------------------------------

        #Perform every 500 milliseconds
        #-------------------------------------------------
        #-------------------------------------------------

        #Perform every 1 second
        #-------------------------------------------------
        #-------------------------------------------------

        

#/////////////////////////////////////////////////////////