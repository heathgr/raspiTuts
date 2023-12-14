#!/usr/bin/python3

from gpiozero import LightSensor
from time import sleep
import atexit


def cleanExit():
    pass


atexit.register(cleanExit)

lightSensor = LightSensor(19)

while True:
    lightValue = lightSensor.value
    print(f"light value: {lightValue}")
    sleep(0.2)
