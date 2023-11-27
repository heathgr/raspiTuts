#!/usr/bin/python3

from store import Store
from display import Display
from time import sleep
import atexit

from multiprocessing import Process

state = Store({
    "temp": 0,
    "triggerPoint": 15,
    "triggerLessThan": True,
})

display = Display()
display.register(state)


class Test:
    def __init__(self, state):
        self.__state = state

    def task1(self):
        while True:
            self.__state.update({"temp": 5})
            sleep(3)

    def task2(self):
        while True:
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


def cleanExit():
    display.clear()


atexit.register(cleanExit)

test = Test(state)

test.start()

sleep(30)

test.stop()
