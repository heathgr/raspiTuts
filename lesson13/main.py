#!/usr/bin/python3

from RPi import GPIO
from time import sleep
from utils import hsv_to_rgb
import atexit

LED_BLUE = 40
LED_GREEN = 38
LED_RED = 36

SWITCH_RESET = 26
SWITCH_VALUE = 24
SWITCH_SATURATION = 22
SWITCH_HUE = 18

MAX_HUE_LEVEL = 5
MAX_SATURATION_LEVEL = 3
MAX_VALUE_LEVEL = 5

hueLevel = 0
saturationLevel = 3
valueLevel = 5
rPwmAgent = None
gPwmAgent = None
bPwmAgent = None


def exitHandler():
    print("Cleaning up GPIO configuration.")
    GPIO.cleanup()


def setLeds():
    rgbValues = hsv_to_rgb(
        hueLevel / MAX_HUE_LEVEL,
        saturationLevel / MAX_SATURATION_LEVEL,
        valueLevel / MAX_VALUE_LEVEL,
    )

    rPwmAgent.ChangeDutyCycle(round(rgbValues[0] * 100))
    gPwmAgent.ChangeDutyCycle(round(rgbValues[1] * 100))
    bPwmAgent.ChangeDutyCycle(round(rgbValues[2] * 100))


def onResetPressed(channel):
    print("Reset")


def onHuePressed(channel):
    hueLevel += 1
    if (hueLevel > MAX_HUE_LEVEL):
        hueLevel = 0


def onSaturationPressed(channel):
    print("Saturation")


def onValuePressed(channel):
    print("Value")


def init():
    global rPwmAgent
    global gPwmAgent
    global bPwmAgent

    print("Initializing....")
    atexit.register(exitHandler)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(SWITCH_RESET, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(SWITCH_VALUE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(SWITCH_HUE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(SWITCH_SATURATION, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(LED_BLUE, GPIO.OUT)
    GPIO.setup(LED_GREEN, GPIO.OUT)
    GPIO.setup(LED_RED, GPIO.OUT)
    rPwmAgent = GPIO.PWM(LED_RED, 2000)
    gPwmAgent = GPIO.PWM(LED_GREEN, 2000)
    bPwmAgent = GPIO.PWM(LED_BLUE, 2000)
    GPIO.add_event_detect(
        SWITCH_RESET,
        GPIO.FALLING,
        callback=onResetPressed,
        bouncetime=300
    )
    GPIO.add_event_detect(
        SWITCH_VALUE,
        GPIO.FALLING,
        callback=onValuePressed,
        bouncetime=300
    )
    GPIO.add_event_detect(
        SWITCH_SATURATION,
        GPIO.FALLING,
        callback=onSaturationPressed,
        bouncetime=300
    )
    GPIO.add_event_detect(
        SWITCH_HUE,
        GPIO.FALLING,
        callback=onHuePressed,
        bouncetime=300
    )
    setLeds()


def start():
    print("starting...")
    while True:
        sleep(1)


init()
start()
