#!/usr/bin/python3

from store import Store
from display import Display
from time import sleep
import atexit

from multiprocessing import Process
from gpiozero import MCP3008

state = Store({
    "temp": 0,
    "triggerPoint": 15,
    "triggerLessThan": True,
})

display = Display()
display.register(state)


def cleanExit():
    display.clear()


atexit.register(cleanExit)


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

potentiometer = MCP3008(0)

while True:
    value = potentiometer.value()
    print(f"value: {value}")
    sleep(0.2)
