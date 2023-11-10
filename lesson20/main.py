#!/usr/bin/python3

from gpiozero import MCP3008
from time import sleep

potentiometer = MCP3008(0)

while True:
    print(f"potentiometer value: {potentiometer}")
    sleep(0.2)
