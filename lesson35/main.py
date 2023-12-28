#!/usr/bin/python3

from keypad import Keypad
from store import Store
from display import Display
from appModes import AppModes


appState = Store({
    "appMode": AppModes.DISARMED,
    "keypadInput": "",
})

myKeypad = Keypad()
myDisplay = Display()


def onKeypadInput(value):
    if value == "A":
        appState.update({"appMode": AppModes.ARMED})
        return

    if value == "B":
        appState.update({"appMode": AppModes.DISARMED})
        return


myDisplay.subscribe(appState)
myKeypad.onChange = onKeypadInput
