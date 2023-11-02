#!/usr/bin/python3

import RPi.GPIO as GPIO
import atexit
from time import sleep

SWITCH_DOWN = 36
SWITCH_UP = 38
LED_0 = 40
INCREMENT_AMOUNT = 10 / 6


def exitHandler():
    print("Cleaning up GPIO configuration.")
    GPIO.cleanup()


GPIO.setmode(GPIO.BOARD)
GPIO.setup(SWITCH_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_UP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_0, GPIO.OUT)
atexit.register(exitHandler)

pwmAgent = GPIO.PWM(LED_0, 2000)
ledState = 0
upState = 0
downState = 0

pwmAgent.start(ledState)

while True:
    inputUp = GPIO.input(SWITCH_UP)
    inputDown = GPIO.input(SWITCH_DOWN)

    if upState == 0 and inputUp == 1:
        ledState += INCREMENT_AMOUNT
    if downState == 0 and inputDown == 1:
        ledState -= INCREMENT_AMOUNT
    if ledState < 0:
        ledState = 0
    if ledState > 100:
        ledState = 100

    pwmAgent.ChangeDutyCycle(ledState)
    upState = inputUp
    downState = inputDown

    sleep(0.1)
