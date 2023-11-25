#!/usr/bin/python3

from time import sleep
from RPi import GPIO
import atexit

BUZZER = 26


def cleanExit():
    print("Cleaning up GPIO.")
    GPIO.cleanup()


atexit.register(cleanExit)

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)

buzzPwm = GPIO.PWM(BUZZER, 400)
buzzPwm.start(0)

while True:
    for i in range(150, 2000):
        buzzPwm.ChangeFrequency(i)
        sleep(0.0001)
    for i in range(2000, 150, -1):
        buzzPwm.ChangeFrequency(i)
        sleep(0.0001)
