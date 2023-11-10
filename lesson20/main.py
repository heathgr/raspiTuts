#!/usr/bin/python3

from gpiozero import MCP3008, Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

potentiometer = MCP3008(0)
factory = PiGPIOFactory()
servo = Servo(26, pin_factory=factory, frame_width=0.02,
              min_pulse_width=0.0005, max_pulse_width=0.0025)

while True:
    value = -(potentiometer.value * 2.0) + 1.0
    servo.value = value
    print(f"value: {value}")
    sleep(0.2)
