#!/usr/bin/python3

from store import Store
from display import Display
from potentiometer import Potentiometer
from time import sleep
import atexit

state = Store({
    "temp": 0,
    "triggerPoint": 15,
    "triggerLessThan": True,
})

display = Display()
display.register(state)
alarmDial = Potentiometer(0)


def cleanExit():
    display.clear()


atexit.register(cleanExit)


def onalarmDialChange(value):
    print(f"dial value: {value}")


alarmDial.onChange(onalarmDialChange)

while True:
    sleep(0.2)
