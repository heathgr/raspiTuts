#!/usr/bin/python3

from keypad import Keypad

myKeypad = Keypad()

keypadInput = ""

while True:
    keypressed = myKeypad.input()
    if keypressed == "D":
        print(f"Input code: {keypadInput}")
        keypadInput = ""
    if keypressed != "D":
        keypadInput += keypressed
