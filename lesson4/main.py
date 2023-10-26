import RPi.GPIO as GPIO
import time
import atexit
from utils import getValidatedInput, positiveIntValidator, yesOrNoValidator

def init():
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(11, GPIO.OUT)
  atexit.register(exitHandler)

def exitHandler():
  print("Cleaning up GPIO configuration.")
  GPIO.cleanup()

def setLight(value):
  GPIO.output(11, value)

init()

isRunning = True

while isRunning:
  numberOfBlinks = getValidatedInput(
    "How many times do you want the light to blink? ",
    "You must enter a whole number greater than 0.",
    positiveIntValidator,
  )

  for i in range(0, numberOfBlinks):
    print(f"Blinking light {i + 1} times out of {numberOfBlinks}")
    setLight(True)
    time.sleep(0.5)
    setLight(False)
    time.sleep(0.5)
  
  print("That was fun :)\n")

  isRunning = getValidatedInput(
    "Run again? ",
    "You must answer with y or n.",
    yesOrNoValidator,
  )