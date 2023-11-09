#!/usr/bin/python3

from gpiozero import Servo
from time import sleep

servo = Servo(26)

while True:
    value = float(input("Servo Value: "))
    servo.value = value
    sleep(2)
