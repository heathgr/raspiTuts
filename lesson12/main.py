#!/usr/bin/python3

from RPi import GPIO
from time import sleep
import atexit

LED_BLUE = 40
LED_RED = 38
LED_GREEN = 36

SWITCH_ALL_OFF = 28
SWITCH_BLUE = 26
SWITCH_GREEN = 24
SWITCH_RED = 22


def exitHandler():
    print("Cleaning up GPIO configuration.")
    GPIO.cleanup()


def allOffHandler():
    print("all off!!!!")


def init():
    print("Initializing....")
    atexit.register(exitHandler)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(SWITCH_ALL_OFF, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(
        SWITCH_ALL_OFF,
        GPIO.FALLING,
        callback=allOffHandler,
        bouncetime=300
    )


def start():
    print("starting...")
    while True:
        sleep(1)


init()
start()
