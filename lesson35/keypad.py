from gpiozero import OutputDevice, InputDevice, TonalBuzzer
from gpiozero.tones import Tone
from threading import Thread
from time import sleep


class Keypad:
    keypadValues = [
        '1', '2', '3', 'A',
        '4', '5', '6', 'B',
        '7', '8', '9', 'C',
        '*', '0', '#', 'D',
    ]

    def __init__(self, columPins=[21, 20, 16, 12], rowPins=[19, 13, 6, 5], buzzerPin=26):
        self.onChange = None
        self.__columns = map(lambda x: OutputDevice(x), columPins)
        self.__rows = map(lambda x: InputDevice(x), rowPins)
        self.__buzzer = TonalBuzzer(buzzerPin)
        self.__monitorProcess = Thread(target=self.monitor)
        self.__monitorProcess.start()

    def monitor(self):
        while True:
            keypadInput = self.input
            if self.onChange:
                self.onChange(keypadInput)

    def input(self):
        keyPressedValue = None

        while True:
            wasPressed = 0

            for rid, row in enumerate(self.__rows):
                for cid, column in enumerate(self.__columns):
                    column.on()
                    isPressed = row.value
                    column.off()
                    if isPressed:
                        valueIndex = (rid * 4) + cid
                        keyPressedValue = self.keypadValues[valueIndex]
                        self.__buzzer.play(Tone(500))
                        wasPressed = 1
            if not wasPressed and keyPressedValue:
                self.__buzzer.stop()
                return keyPressedValue
            sleep(0.01)
