#!/usr/bin/python3

from keypad import Keypad
import LCD1602 as LCD

myKeypad = Keypad()

keypadInput = ""

LCD.init(0X27, 1)
LCD.write(0, 0, "Hello")
LCD.write(0, 1, "World")

while True:
    keypressed = myKeypad.input()
    if keypressed == "D":
        print(f"Input code: {keypadInput}")
        keypadInput = ""
    if keypressed != "D":
        keypadInput += keypressed
