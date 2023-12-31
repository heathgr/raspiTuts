#!/usr/bin/python3

import RPi.GPIO as GPIO
import atexit
from time import sleep

SWITCH_DOWN = 36
SWITCH_UP = 38
LED_0 = 40
NUMBER_OF_INCREMENTS = 6
MAX_LED_LEVEL = NUMBER_OF_INCREMENTS - 1
INCREMENT_CONVERSION_EXPONENT = 10**(2/MAX_LED_LEVEL)


def exitHandler():
    print("Cleaning up GPIO configuration.")
    GPIO.cleanup()


GPIO.setmode(GPIO.BOARD)
GPIO.setup(SWITCH_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_UP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_0, GPIO.OUT)
atexit.register(exitHandler)

pwmAgent = GPIO.PWM(LED_0, 2000)
ledLevel = 0
upState = 0
downState = 0

pwmAgent.start(ledLevel)

while True:
    inputUp = GPIO.input(SWITCH_UP)
    inputDown = GPIO.input(SWITCH_DOWN)

    if upState == 0 and inputUp == 1:
        ledLevel += 1
    if downState == 0 and inputDown == 1:
        ledLevel -= 1
    if ledLevel < 0:
        ledLevel = 0
    if ledLevel > MAX_LED_LEVEL:
        ledLevel = MAX_LED_LEVEL

    if (ledLevel == 0):
        pwmAgent.ChangeDutyCycle(0)
    if (ledLevel != 0):
        dc = round(INCREMENT_CONVERSION_EXPONENT**ledLevel)
        print(f"dc value:{dc} led level:{ledLevel}")
        pwmAgent.ChangeDutyCycle(dc)
    upState = inputUp
    downState = inputDown

    sleep(0.1)
