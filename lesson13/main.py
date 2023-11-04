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


class LedController:
    def __init__(self):
        print("Initializing Led Controller....")
        self.__hueLevel = 0
        self.__saturationLevel = 3
        self.__valueLevel = 5
        self.isRunning = True

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(SWITCH_RESET, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(SWITCH_VALUE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(SWITCH_HUE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(SWITCH_SATURATION, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(LED_BLUE, GPIO.OUT)
        GPIO.setup(LED_GREEN, GPIO.OUT)
        GPIO.setup(LED_RED, GPIO.OUT)

        self.__rPwmAgent = GPIO.PWM(LED_RED, 2000)
        self.__gPwmAgent = GPIO.PWM(LED_GREEN, 2000)
        self.__bPwmAgent = GPIO.PWM(LED_BLUE, 2000)

        GPIO.add_event_detect(
            SWITCH_RESET,
            GPIO.FALLING,
            callback=self.onResetPressed,
            bouncetime=300
        )
        GPIO.add_event_detect(
            SWITCH_VALUE,
            GPIO.FALLING,
            callback=self.onValuePressed,
            bouncetime=300
        )
        GPIO.add_event_detect(
            SWITCH_SATURATION,
            GPIO.FALLING,
            callback=self.onSaturationPressed,
            bouncetime=300
        )
        GPIO.add_event_detect(
            SWITCH_HUE,
            GPIO.FALLING,
            callback=self.onHuePressed,
            bouncetime=300
        )
        self.setLeds()
        print("Ready :)")

    def setLeds(self):
        rgbValues = hsv_to_rgb(
            self.__hueLevel / MAX_HUE_LEVEL,
            self.__saturationLevel / MAX_SATURATION_LEVEL,
            self.__valueLevel / MAX_VALUE_LEVEL,
        )

        print(
            f"New RGB values: R {rgbValues[0]} G {rgbValues[1]} B {rgbValues[2]}")

        self.__rPwmAgent.ChangeDutyCycle(100)
        self.__gPwmAgent.ChangeDutyCycle(100)
        self.__bPwmAgent.ChangeDutyCycle(100)
        # self.__rPwmAgent.ChangeDutyCycle(round(rgbValues[0] * 100))
        # self.__gPwmAgent.ChangeDutyCycle(round(rgbValues[1] * 100))
        # self.__bPwmAgent.ChangeDutyCycle(round(rgbValues[2] * 100))

    def onResetPressed(self, channel):
        print("Reset")

    def onHuePressed(self, channel):
        print("Hue Pressed")
        self.__hueLevel += 1
        if (self.__hueLevel > MAX_HUE_LEVEL):
            self.__hueLevel = 0
        self.setLeds()

    def onSaturationPressed(self, channel):
        print("Saturation")

    def onValuePressed(self, channel):
        print("Value")


def exitHandler():
    print("Cleaning up GPIO configuration.")
    GPIO.cleanup()


def start():
    atexit.register(exitHandler)
    print("starting...")
    controller = LedController()
    while controller.isRunning:
        sleep(1)


start()
