from dht11 import DHT11
from threading import Thread
from time import sleep


class TempSensor:
    def __init__(self, pin):
        self.__sensor = DHT11(pin=pin)
        self.__process = Thread(target=self.processHandler)
        self.__value = None
        self.onChange = None
        self.__process.start()

    def processHandler(self):
        while True:
            if self.onChange:
                reading = self.__sensor.read()
                if reading.is_valid():
                    newValue = round((reading.temperature * 1.8) + 32, 2)
                    if newValue != self.__value:
                        self.onChange(newValue)
                    self.__value = newValue
            sleep(1)
