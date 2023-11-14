#!/usr/bin/python3

from RPi import GPIO
from time import sleep
import atexit

PIR = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)


def cleanExit():
    print("Doing a GPIO cleanup.")
    GPIO.cleanup()


atexit.register(cleanExit)

print("Initializing hold on to your butts!!!!")
sleep(10)

while True:
    hasMotion = GPIO.input(PIR)
    print(f"is moving: {hasMotion}")
    sleep(0.2)
