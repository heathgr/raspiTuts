#!/usr/bin/python3

import RPi.GPIO as GPIO
import atexit
from time import sleep

SWITCH_DOWN = 36
SWITCH_UP = 38
LED_0 = 40


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

pwmAgent.start(ledState)

while True:
    input_up = GPIO.input(SWITCH_UP)
    input_down = GPIO.input(SWITCH_DOWN)

    if input_up:
        ledState += 20
    if input_down:
        ledState -= 20
    if ledState < 0:
        ledState = 0
    if ledState > 100:
        ledState = 100

    pwmAgent.ChangeDutyCycle(ledState)

    sleep(0.1)
