#!/usr/bin/python3

import RPi.GPIO as GPIO
import ADC0834
import time
from utils import hsv_to_rgb

LED_BLUE = 26
LED_GREEN = 19
LED_RED = 13

GPIO.setmode(GPIO.BCM)
ADC0834.setup()
GPIO.setup(LED_BLUE, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.setup(LED_RED, GPIO.OUT)

rPwmAgent = GPIO.PWM(LED_RED, 2000)
gPwmAgent = GPIO.PWM(LED_GREEN, 2000)
bPwmAgent = GPIO.PWM(LED_BLUE, 2000)

rPwmAgent.start(0)
gPwmAgent.start(0)
bPwmAgent.start(0)

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
        print(f"r: {rgb[0]} g: {rgb[1]} b: {rgb[2]}")
        rPwmAgent.ChangeDutyCycle(int(rgb[0] * 100))
        gPwmAgent.ChangeDutyCycle(int(rgb[1] * 100))
        bPwmAgent.ChangeDutyCycle(int(rgb[2] * 100))
        time.sleep(.2)

except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Good to Go')
