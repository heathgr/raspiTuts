#!/usr/bin/python3

from store import Store
from display import Display
from time import sleep
import atexit

state = Store({
    "temp": 0,
    "triggerPoint": 15,
    "triggerLessThan": True,
})

display = Display()
display.register(state)

sleep(1)
state.update({"temp": 20})
sleep(1)
state.update({"temp": 25})


def cleanExit():
    display.clear()


atexit.register(cleanExit)

while True:
    sleep(1)
