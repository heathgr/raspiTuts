#!/usr/bin/python3

from store import Store
from display import Display
from potentiometer import Potentiometer
from time import sleep
import atexit

state = Store({
    "temp": 0,
    "triggerPoint": 15,
    "triggerLessThan": True,
})

display = Display()
display.register(state)
alarmDial = Potentiometer(0)


def cleanExit():
    display.clear()


atexit.register(cleanExit)


def onalarmDialChange(value):
    print(f"dial value: {value}")


alarmDial.onChange(onalarmDialChange)


class Test:
    def __init__(self, state):
        self.__state = state

    def task1(self):
        while True:
            print("task 1 running.")
            self.__state.update({"temp": 5})
            sleep(3)

    def task2(self):
        while True:
            print("task 2 running.")
            self.__state.update({"temp": 8})
            sleep(1.87)

    def start(self):
        self.__proc1 = Process(target=self.task1)
        self.__proc2 = Process(target=self.task2)

        self.__proc1.start()
        self.__proc2.start()

    def stop(self):
        self.__proc1.kill()
        self.__proc2.kill()


# test = Test(state)

# test.start()

# sleep(30)

# test.stop()

while True:
    sleep(0.2)
