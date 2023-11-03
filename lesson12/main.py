#!/usr/bin/python3

from RPi import GPIO
from time import sleep
import atexit

LED_BLUE = 40
LED_GREEN = 38
LED_RED = 36

SWITCH_ALL_OFF = 26
SWITCH_BLUE = 24
SWITCH_GREEN = 22
SWITCH_RED = 18

LED_FROM_SWITCH = {
    SWITCH_BLUE: LED_BLUE,
    SWITCH_GREEN: LED_GREEN,
    SWITCH_RED: LED_RED,
}


def exitHandler():
    print("Cleaning up GPIO configuration.")
    GPIO.cleanup()


def onAllOffPressed(channel):
    print("all off pressed!!!!")


def onToggleLed(channel):
    ledPin = LED_FROM_SWITCH[channel]

    print(f"Toggle pressed! button pin: {channel} led pin: {ledPin}")
    GPIO.output(ledPin, not GPIO.input(ledPin))


def init():
    print("Initializing....")
    atexit.register(exitHandler)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(SWITCH_ALL_OFF, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(SWITCH_BLUE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(SWITCH_RED, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(SWITCH_GREEN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(LED_BLUE, GPIO.OUT)
    GPIO.setup(LED_GREEN, GPIO.OUT)
    GPIO.setup(LED_RED, GPIO.OUT)
    GPIO.add_event_detect(
        SWITCH_ALL_OFF,
        GPIO.FALLING,
        callback=onAllOffPressed,
        bouncetime=300
    )
    GPIO.add_event_detect(
        SWITCH_BLUE,
        GPIO.FALLING,
        callback=onToggleLed,
        bouncetime=300
    )
    GPIO.add_event_detect(
        SWITCH_GREEN,
        GPIO.FALLING,
        callback=onToggleLed,
        bouncetime=300
    )
    GPIO.add_event_detect(
        SWITCH_RED,
        GPIO.FALLING,
        callback=onToggleLed,
        bouncetime=300
    )


def start():
    print("starting...")
    while True:
        sleep(1)


init()
start()
