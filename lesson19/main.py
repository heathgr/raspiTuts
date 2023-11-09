#!/usr/bin/python3

from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory()
servo = Servo(26, pin_factory=factory, frame_width=0.02, min_pulse_width=0.0005, max_pulse_width=0.0025)

while True:
    value = float(input("Servo Value: "))
    servo.value = value
    sleep(0.2)
