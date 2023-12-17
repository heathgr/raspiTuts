#!/usr/bin/python3

from gpiozero import OutputDevice, InputDevice
from time import sleep

# columns
columns = OutputDevice(21)
# rows
rows = InputDevice(19)

while True:
    columns.on()
    value = rows.value
    columns.off()
    print(f"test: {value}")
    sleep(0.2)
