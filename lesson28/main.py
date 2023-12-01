#!/usr/bin/python3

from store import Store
from display import Display
from potentiometer import Potentiometer
from gpiozero import Button
from time import sleep, time
import atexit

state = Store({
    "temp": 0,
    "triggerPoint": 0,
    "triggerLessThan": True,
    "isEditable": False,
    "togglePressedTime": 0,
})

TOGGLE_HOLD_TIME = 0.5

display = Display()
display.subscribe(state)
alarmDial = Potentiometer(0)
alarmToggle = Button(19, pull_up=False, hold_time=TOGGLE_HOLD_TIME)


def cleanExit():
    display.clear()


atexit.register(cleanExit)


def alarmDialChanged(value):
    if state.state["isEditable"]:
        state.update({"triggerPoint": round((1 - value) * 100, 0)})


def toggleHeld():
    state.update({"isEditable": not state.state["isEditable"]})


def togglePressed():
    state.update({"togglePressedTime": time()})


def toggleReleased():
    if (time() - state.state["togglePressedTime"]) > 0.5:
        return
    if state.state["isEditable"]:
        state.update({"triggerLessThan": not state.state["triggerLessThan"]})


alarmToggle.when_pressed = togglePressed
alarmToggle.when_released = toggleReleased
alarmToggle.when_held = toggleHeld

alarmDial.onChange = alarmDialChanged

print("Initialized!!!")

while True:
    sleep(0.2)
