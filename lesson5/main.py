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

def intToBinaryArray(value):
  x = value
  result = [0] * 5
  
  for i in range(0, 5):
    result[4 - i] = floor(x % 2)
    x = x * 0.5

  return result

init()

while True:
  for i in range(0, 32):
    ledStates = intToBinaryArray(i)
    
    setLight(LED_0, ledStates[0])
    setLight(LED_1, ledStates[1])
    setLight(LED_2, ledStates[2])
    setLight(LED_3, ledStates[3])
    setLight(LED_4, ledStates[4])
    sleep(1)