from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep


class Buzzer:
    def __init__(self, pin):
        self.__buzzer = TonalBuzzer(pin)
        sleep(3)
        self.__buzzer.play(Tone("A4"))
        sleep(0.5)
        self.__buzzer.play(Tone("C3"))
        sleep(0.5)
        self.__buzzer.stop()
        pass

    def subscribe(self, store):
        store.subscribe(self.update)
        self.update(store.state)

    def update(self, state):
        pass
