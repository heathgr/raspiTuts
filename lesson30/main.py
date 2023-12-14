#!/usr/bin/python3

from gpiozero import LightSensor, SmoothedInputDevice
from time import sleep
import atexit


def cleanExit():
    pass


atexit.register(cleanExit)

lightSensor = LightSensor(19)
motionSensor = SmoothedInputDevice(13)

while True:
    lightValue = lightSensor.value
    motionValue = motionSensor.value
    print(f"light value: {lightValue} motion value: {motionValue}")
    sleep(0.2)
