#!/usr/bin/python3

import RPi.GPIO as GPIO
import atexit
from time import sleep

SERVO = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO, GPIO.OUT)

servoPwm = GPIO.PWM(SERVO, 50)
servoPwm.start(0)


def cleanup():
    GPIO.cleanup()
    print('GPIO Good to Go')


atexit.register(cleanup)

while True:
    value = float(input("PWM Value: "))
    servoPwm.ChangeDutyCycle(value)
    sleep(.1)
