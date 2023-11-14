#!/usr/bin/python3

from RPi import GPIO
from time import sleep
from dht11 import DHT11
import atexit


def cleanExit():
    print("Cleaning up GPIO.")
    GPIO.cleanup()


atexit.register(cleanExit)

SENSOR_PIN = 21

GPIO.setmode(GPIO.BCM)
sensor = DHT11(pin=SENSOR_PIN)

while True:
    value = sensor.read()
    if value.is_valid():
        print(f"Temp: {(value.temperature * 1.8) + 32} Humidity: {value.humidity}")
    sleep(0.2)
