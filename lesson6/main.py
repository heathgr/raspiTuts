#!/usr/bin/python3

import RPi.GPIO as GPIO
import atexit
from time import sleep

SWITCH = 23
LED_0 = 29


def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(SWITCH, GPIO.IN)
    GPIO.setup(LED_0, GPIO.OUT)
    atexit.register(exitHandler)


def exitHandler():
    print("Cleaning up GPIO configuration.")
    GPIO.cleanup()


init()

while True:
    readValue = GPIO.input(SWITCH)
    GPIO.output(LED_0, readValue)
    print(readValue)
    sleep(0.1)
