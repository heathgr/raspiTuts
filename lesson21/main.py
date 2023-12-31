#!/usr/bin/python3

from time import sleep, time
from RPi import GPIO
import atexit


def cleanExit():
    print("Cleaning GPIO")
    GPIO.cleanup()


atexit.register(cleanExit)

TRIGGER = 26
ECHO = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

while True:
    GPIO.output(TRIGGER, 0)
    sleep(2E-6)
    GPIO.output(TRIGGER, 1)
    sleep(10E-6)
    GPIO.output(TRIGGER, 0)
    while GPIO.input(ECHO) == 0:
        pass
    echoStartTime = time()
    while GPIO.input(ECHO) == 1:
        pass
    echoEndTime = time()
    # print((echoEndTime - echoStartTime) * 13397.24409)
    print((echoEndTime - echoStartTime) * 13499.2)
    sleep(0.2)
