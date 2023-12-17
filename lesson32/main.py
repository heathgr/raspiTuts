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

while True:
    columnValue = None
    rowValue = None

    for rid, row in enumerate(rows):
        for cid, column in enumerate(columns):
            column.on()
            isPressed = row.value
            column.off()
            if isPressed:
                print(f"row: {rid} column: {cid}")
    sleep(0.2)
