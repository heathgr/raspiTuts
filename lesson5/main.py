#!/usr/bin/python3

import RPi.GPIO as GPIO
import atexit
from time import sleep
from math import floor

LED_0 = 29
LED_1 = 31
LED_2 = 33
LED_3 = 35
LED_4 = 37

def init():
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(LED_0, GPIO.OUT)
  GPIO.setup(LED_1, GPIO.OUT)
  GPIO.setup(LED_2, GPIO.OUT)
  GPIO.setup(LED_3, GPIO.OUT)
  GPIO.setup(LED_4, GPIO.OUT)
  atexit.register(exitHandler)

def exitHandler():
  print("Cleaning up GPIO configuration.")
  GPIO.cleanup()

def setLight(led, value):
  GPIO.output(led, value)

init()

setLight(LED_0, True)
setLight(LED_1, True)
setLight(LED_2, True)
setLight(LED_3, True)
setLight(LED_4, True)

sleep(3)

setLight(LED_0, False)
setLight(LED_1, False)
setLight(LED_2, False)
setLight(LED_3, False)
setLight(LED_4, False)