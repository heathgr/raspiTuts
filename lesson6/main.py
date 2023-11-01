#!/usr/bin/python3

import RPi.GPIO as GPIO
import atexit
from time import sleep

SWITCH = 29

def init():
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(SWITCH, GPIO.IN)
  atexit.register(exitHandler)

def exitHandler():
  print("Cleaning up GPIO configuration.")
  GPIO.cleanup()

init()

while True:
  readValue = GPIO.input(SWITCH)
  print(readValue)
  sleep(0.1)