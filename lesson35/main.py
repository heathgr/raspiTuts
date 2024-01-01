#!/usr/bin/python3

from keypad import Keypad
from store import Store
from display import Display
from appModes import AppModes


appState = Store({
    "appMode": AppModes.DISARMED,
    "keypadInput": "",
    "password": "5555",
    "newPassword1": "",
    "newPassword2": "",
    "isArmed": False,
})

myKeypad = Keypad()
myDisplay = Display()


def onKeypadInput(value):
    appMode = appState.state["appMode"]

    if value == "A":
        appState.update({
            "appMode": AppModes.ARMED,
            "keypadInput": "",
            "isArmed": True,
        })
        return
    elif value == "B" and appMode != AppModes.REQUEST_DISARM:
        appState.update({
            "appMode": AppModes.REQUEST_DISARM,
            "keypadInput": "",
        })
        return
    elif value == "C" and appMode != AppModes.REQUEST_PASSWORD_CHANGE:
        appState.update({
            "appMode": AppModes.REQUEST_PASSWORD_CHANGE,
            "keypadInput": "",
        })
        return
    # TODO use a regex instead of isnumeric so the password can contain # and * characters
    elif value.isnumeric():
        keypadInput = appState.state["keypadInput"]
        appMode = appState.state["appMode"]

        keypadInput = keypadInput + "value"

        if len(keypadInput) == 4:
            print(f"veryify password: {keypadInput}")
            if appMode == AppModes.REQUEST_DISARM:
                if keypadInput == appState["password"]:
                    appState.update({
                        "appMode": AppModes.DISARMED,
                        "isArmed": False,
                        "keypadInput": "",
                    })
        else:
            appState.update({
                "keypadInput": keypadInput
            })


myDisplay.subscribe(appState)
myKeypad.onChange = onKeypadInput
