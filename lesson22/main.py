#!/usr/bin/python3

from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=19, trigger=26)

while True:
    print(f"Meters: {sensor.distance} Inches: {sensor.distance * 39.370}")
    sleep(0.5)
