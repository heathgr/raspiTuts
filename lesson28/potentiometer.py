from threading import Thread
from gpiozero import MCP3008
from time import sleep


class Potentiometer:
    def __init__(self, channel):
        self.onChange = None
        self.__potentiometer = MCP3008(channel)
        self.__process = Thread(target=self.processHandler)
        self.__value = None
        self.__process.start()

    def processHandler(self):
        while True:
            if self.onChange:
                newValue = round(self.__potentiometer.value, 2)
                if newValue != self.__value:
                    self.onChange(newValue)
                self.__value = newValue
            sleep(0.2)

    @property
    def value(self):
        return self.__value
