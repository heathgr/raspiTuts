from multiprocessing import Process
from gpiozero import MCP3008
from time import sleep


class Potentiometer:
    def __init__(self, channel):
        self.__potentiometer = MCP3008(channel)
        self.__process = Process(target=self.processHandler)
        self.__value = None
        self.__process.start()
        self.onChange = None

    def processHandler(self):
        while True:
            if self.onChange != None:
                print("checking pot value")
                newValue = round(self.__potentiometer.value, 2)
                if newValue != self.__value:
                    self.onChange(newValue)
                self.__value = newValue
            else:
                print("onchange not set")
            sleep(0.2)

    @property
    def value(self):
        return self.__value
