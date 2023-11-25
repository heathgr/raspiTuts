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

while True:
    GPIO.output(BUZZER, 0)
    sleep(1)
    GPIO.output(BUZZER, 1)
    sleep(1)
