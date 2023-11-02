#!/usr/bin/python3

from RPi import GPIO
from time import sleep
import atexit

LED_BLUE = 40
LED_RED = 38
LED_GREEN = 36

SWITCH_ALL_OFF = 26
SWITCH_BLUE = 24
SWITCH_GREEN = 22
SWITCH_RED = 18


def exitHandler():
    print("Cleaning up GPIO configuration.")
    GPIO.cleanup()


def allOffHandler(channel):
    print(f"channel {channel} was pressed.")
    print("all off!!!!")


def init():
    print("Initializing....")
    atexit.register(exitHandler)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(SWITCH_ALL_OFF, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(
        SWITCH_ALL_OFF,
        GPIO.RISING,
        callback=allOffHandler,
        bouncetime=300
    )


def start():
    print("starting...")
    while True:
        sleep(1)


init()
start()
