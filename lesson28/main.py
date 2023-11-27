#!/usr/bin/python3

from store import Store
from display import Display
from time import sleep

state = store({
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
