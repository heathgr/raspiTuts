#!/usr/bin/python3

from gpiozero import OutputDevice, InputDevice, TonalBuzzer
from gpiozero.tones import Tone
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

buzzer = TonalBuzzer(26)

keypadValues = [
    '1', '2', '3', 'A',
    '4', '5', '6', 'B',
    '7', '8', '9', 'C',
    '*', '0', '#', 'D',
]

keypadTones = [
    Tone(400.0), Tone(420.0), Tone(440.0), Tone(460.0),
    Tone(480.0), Tone(500.0), Tone(520.0), Tone(540.0),
    Tone(560.0), Tone(580.0), Tone(600.0), Tone(620.0),
    Tone(640.0), Tone(660.0), Tone(680.0), Tone(700.0),
]

keyPressedValue = None

while True:
    wasPressed = 0

    for rid, row in enumerate(rows):
        for cid, column in enumerate(columns):
            column.on()
            isPressed = row.value
            column.off()
            if isPressed:
                valueIndex = (rid * 4) + cid
                keyPressedValue = keypadValues[valueIndex]
                buzzer.play(keypadTones[valueIndex])
                wasPressed = 1
    if not wasPressed and keyPressedValue:
        print(f"key: {keyPressedValue}")
        keyPressedValue = None
        buzzer.stop()
    sleep(0.01)
