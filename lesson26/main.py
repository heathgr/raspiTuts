#!/usr/bin/python3

from time import sleep
from RPi import GPIO
from dht11 import DHT11
import LCD1602 as LCD
import atexit


def cleanExit():
    sleep(0.2)
    print("Cleaning up LCD Display.")
    LCD.clear()
    print("Cleaning up GPIO.")
    GPIO.cleanup()


atexit.register(cleanExit)

TOGGLE_BUTTON = 20

GPIO.setmode(GPIO.BCM)
LCD.init(0X27, 1)
sensor = DHT11(pin=21)

showF = False


def onToggle(channel):
    global showF

    showF = not showF


GPIO.setup(TOGGLE_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(
    TOGGLE_BUTTON,
    GPIO.FALLING,
    callback=onToggle,
    bouncetime=300
)

while True:
    value = sensor.read()
    if value.is_valid():
        print(f"Temp: {value.temperature} Humidity: {value.humidity}")
        if not showF:
            LCD.write(0, 0, f"Temp: {value.temperature}C")
        if showF:
            LCD.write(
                0, 0, f"Temp: {round((value.temperature * 1.8) + 32, 1)}F")
        LCD.write(0, 1, f"Humidity: {value.humidity}%")
    sleep(0.2)
