#!/usr/bin/python3

import RPi.GPIO as GPIO
import ADC0834
import time

GPIO.setmode(GPIO.BCM)
ADC0834.setup()
try:
    while True:
        hVal = ADC0834.getResult(0)
        sVal = ADC0834.getResult(1)
        lVal = ADC0834.getResult(2)
        print(f"h: {hVal} s: {sVal} l: {lVal}")
        time.sleep(.2)

except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Good to Go')
