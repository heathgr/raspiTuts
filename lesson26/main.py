#!/usr/bin/python3

import LCD1602
import atexit


def cleanExit():
    print("Cleaning up LCD Display.")
    LCD1602.clear()


atexit.register(cleanExit)

LCD1602.init(0X27, 1)

while True:
    LCD1602.write(0, 0, "Hello!!!")
