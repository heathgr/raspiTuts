#!/usr/bin/python3

import RPi.GPIO as GPIO
import ADC0834
import time
from utils import hsv_to_rgb

GPIO.setmode(GPIO.BCM)
ADC0834.setup()
try:
    while True:
        hVal = ADC0834.getResult(0)
        sVal = ADC0834.getResult(1)
        lVal = ADC0834.getResult(2)
        print(f"h: {hVal} s: {sVal} l: {lVal}")
        rgb = hsv_to_rgb(
            hVal / 255,
            sVal / 255,
            lVal / 255
        )
        print(f"r: {rgb[0]} g: {rgb[1]} {rgb[2]}")
        time.sleep(.2)

except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Good to Go')
