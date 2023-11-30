#!/usr/bin/python3

from store import Store
from display import Display
from potentiometer import Potentiometer
from gpiozero import Button
from time import sleep
import atexit

state = Store({
    "temp": 0,
    "triggerPoint": 15,
    "triggerLessThan": True,
    "isEditable": False,
})

display = Display()
display.subscribe(state)
alarmDial = Potentiometer(0)
alarmToggle = Button(19, pull_up=False, hold_time=0.5)


def cleanExit():
    display.clear()


atexit.register(cleanExit)


def alarmDialChanged(value):
    print(f"value: {value}")
    if state.state["isEditable"]:
        state.update({"triggerPoint": round(value * 100, 0)})


def toggleHeld():
    state.update({"isEditable": not state.state["isEditable"]})


def toggleReleased():
    if state.state["isEditable"]:
        state.update({"triggerLessThan": not state.state["triggerLessThan"]})


alarmToggle.when_released = toggleReleased
alarmToggle.when_held = toggleHeld

alarmDial.onChange(alarmDialChanged)

while True:
    sleep(0.2)
