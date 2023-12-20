#!/usr/bin/python3

from keypad import Keypad

myKeypad = Keypad()

while True:
    keypressed = myKeypad.input()
    print(f"key pressed: {keypressed}")
