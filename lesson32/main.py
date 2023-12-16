#!/usr/bin/python3

from gpiozero import OutputDevice, InputDevice
from time import sleep

out = OutputDevice(19)
in = InputDevice(21)

while True:
  out.on()
  value = in.value
  out.off()
  print(f"test: {value}")
  sleep(0.2)
