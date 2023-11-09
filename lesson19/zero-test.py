#!/usr/bin/python3

from gpiozero import AngularServo
from time import sleep

servo = AngularServo(26, min_angle=90, max_angle=90)

while True:
    value = float(input("Servo Angle: "))
    servo.angle = value
    sleep(2)
