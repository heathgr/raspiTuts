#!/usr/bin/python3

from gpiozero import OutputDevice, InputDevice
from time import sleep

columns = [
    OutputDevice(21),
    OutputDevice(20),
    OutputDevice(16),
    OutputDevice(12)
]

rows = [
    InputDevice(19),
    InputDevice(13),
    InputDevice(6),
    InputDevice(5)
]

keypadValues = [
    '1', '2', '3', 'A',
    '4', '5', '6', 'B',
    '7', '8', '9', 'C',
    '*', '0', '#', 'D',
]

keyPressedValue = None
wasPressed = 0

while True:
    for rid, row in enumerate(rows):
        for cid, column in enumerate(columns):
            column.on()
            isPressed = row.value
            column.off()
            if isPressed:
                keyPressedValue = keypadValues[(rid * 4) + cid]
                wasPressed = 1
    if wasPressed and keyPressedValue:
        print(f"key: {keyPressedValue}")
        keyPressedValue = None
        wasPressed = 0
    sleep(0.1)
