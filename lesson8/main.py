#!/usr/bin/python3

import RPi.GPIO as GPIO
import atexit
from time import sleep

SWITCH = 40
LED_0 = 38


def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(LED_0, GPIO.OUT)
    atexit.register(exitHandler)


def exitHandler():
    print("Cleaning up GPIO configuration.")
    GPIO.cleanup()


init()

lastReadValue = 0
ledState = 0

while True:
    readValue = GPIO.input(SWITCH)
    print(readValue)

    if (readValue == 0 and lastReadValue == 1):
        ledState = not ledState
        GPIO.output(LED_0, ledState)

    lastReadValue = readValue
    sleep(0.1)
