from multiprocessing import Process
from gpiozero import MCP3008
from time import sleep


class Potentiometer:
    def __init__(self, channel):
        self.__potentiometer = MCP3008(channel)
        self.__process = Process(target=self.processHandler)

    def onChange(self, callback):
        self.__callback = callback
        self.__process.start()

    def processHandler(self):
        while True:
            newValue = round(self.__potentiometer.value, 2)
            if newValue != self.__value:
                self.__callback(newValue)
            self.__value = newValue
            sleep(0.2)

    @property
    def value(self):
        return self.__value
