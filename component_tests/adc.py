
#7/11/2022: NOT YET TESTED

import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

#Initialize SPI bus. The ADC is the only device using the SPI protocol
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)
mcp = MCP.MCP3008(spi, cs)

#Initialize each sensor as a channel in the ADC:
hrs = AnalogIn(mcp, MCP.P0)
tps = AnalogIn(mcp, MCP.P1)
bps = AnalogIn(mcp, MCP.P2)

while True:
    print("HRS:\t",hrs.value,"\tTPS:\t",tps.value,"\tBPS:\t",bps.value)
    time.sleep(0.25)



