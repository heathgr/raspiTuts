from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from threading import Thread
from time import sleep


class Buzzer:
    def __init__(self, pin):
        self.__buzzer = TonalBuzzer(pin)
        self.__process = Thread(target=self.processHandler)
        self.__process.start()
        pass

    def processHandler(self):
        while True:
            self.__buzzer.play(Tone("A4"))
            sleep(0.3)
            self.__buzzer.play(Tone("C4"))
            sleep(0.3)
            self.__buzzer.stop()
            sleep(0.5)

    def subscribe(self, store):
        store.subscribe(self.update)
        self.update(store.state)

    def update(self, state):
        pass
