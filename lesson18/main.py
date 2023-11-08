#!/usr/bin/python3

import RPi.GPIO as GPIO
import ADC0834
import time

PUSH_BUTTON = 26

GPIO.setmode(GPIO.BCM)
ADC0834.setup()
GPIO.setup(PUSH_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        xVal = ADC0834.getResult(0)
        yVal = ADC0834.getResult(1)
        btnVal = GPIO.input(PUSH_BUTTON)
        print(f"x: {xVal} y: {yVal} button: {btnVal}")
        time.sleep(.2)

except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Good to Go')
