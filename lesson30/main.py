#!/usr/bin/python3

from gpiozero import LightSensor, InputDevice, TonalBuzzer
from gpiozero.tones import Tone
from time import sleep
import atexit


def cleanExit():
    pass


atexit.register(cleanExit)

lightSensor = LightSensor(19)
motionSensor = InputDevice(13)
buzzer = TonalBuzzer(26)

while True:
    lightValue = lightSensor.value
    motionValue = motionSensor.value
    print(f"light value: {lightValue} motion value: {motionValue}")
    if lightValue < 0.5 and motionValue == 1:
        buzzer.play(Tone("A4"))
        sleep(0.2)
        buzzer.play(Tone("C4"))
        sleep(0.2)
    else:
        sleep(0.2)
