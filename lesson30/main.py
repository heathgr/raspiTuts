#!/usr/bin/python3

from gpiozero import LightSensor, InputDevice, TonalBuzzer
from gpiozero.tones import Tone
from time import sleep, time
import atexit


def cleanExit():
    pass


atexit.register(cleanExit)

lightSensor = LightSensor(19)
motionSensor = InputDevice(13)
buzzer = TonalBuzzer(26)

motionTriggeredTime = 0

while True:
    lightValue = lightSensor.value
    motionValue = motionSensor.value

    if motionValue == 1:
        motionTriggeredTime = time()

    timeSinceTrigger = time() - motionTriggeredTime
    print(
        f"light value: {lightValue} motion value: {motionValue} delay: {timeSinceTrigger}")
    if lightValue < 0.5 and timeSinceTrigger < 15:
        buzzer.play(Tone("A4"))
        sleep(0.2)
        buzzer.play(Tone("C4"))
        sleep(0.2)
        buzzer.stop()
    else:
        sleep(0.2)
