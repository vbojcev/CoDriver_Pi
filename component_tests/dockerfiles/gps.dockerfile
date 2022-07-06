FROM python:3

WORKDIR /src

COPY src/gps.py /src/

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip3 install board adafruit-blinka adafruit-circuitpython-gps

RUN python gps.py