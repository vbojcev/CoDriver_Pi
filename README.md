# CoDriver_Pi
The code that runs on CoDriver's microcontroller. CoDriver uses Python and Adafruit's circuitpython libraries to interface with sensors.

component_tests contains python scripts to test the IMU/SWS, GPS, etc.

## Dockerfile Run

After installing Docker on the pi, the code can be run as follows

### gps.dockerfile

```
cd ./component_tests/dockerfiles
docker build -f gps.dockerfile -t gps:test ../
```