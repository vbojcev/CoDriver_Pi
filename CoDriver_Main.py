#IMPORTS
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#Math
import time
import numpy as np
import statistics as stat
from collections import deque

#Hardware interfacing
import board
import busio
import digitalio

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

#Calibrated offsets for the IMU.
IMU_x_adj = 0.5029609161732991
IMU_y_adj = 0.22429359992675774
IMU_z_adj = -1.592849395909651
IMU_ADJ = (IMU_x_adj,IMU_y_adj,IMU_z_adj)

#Calibrated offsets for the SWS.
SWS_x_adj = 0.3495626201558422
SWS_y_adj = 0.0903922856119797
SWS_z_adj = -0.16447526951499292
SWS_ADJ = (SWS_x_adj,SWS_y_adj,SWS_z_adj)

#/////////////////////////////////////////////////////////

#GLOBAL VARIABLES
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#/////////////////////////////////////////////////////////

#FUNCTION DEFINITIONS
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#/////////////////////////////////////////////////////////

#CLASS DEFINITIONS
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#/////////////////////////////////////////////////////////

#MAIN
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
if __name__ == '__main__':
    print("Finished.")
#/////////////////////////////////////////////////////////