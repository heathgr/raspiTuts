#!/usr/bin/python3

from keypad import Keypad
import LCD1602 as LCD

myKeypad = Keypad()

keypadInput = ""

LCD.init(0X27, 1)
LCD.write(0, 0, "Hello")
LCD.write(0, 1, "World")


def onKeypadInput(value):
    print(f"key pressed: {value}")


myKeypad.onChange = onKeypadInput
