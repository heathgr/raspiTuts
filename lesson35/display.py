import LCD1602 as LCD
from appModes import AppModes


class Display:
    def __init__(self):
        LCD.init(0X27, 1)

    def subscribe(self, store):
        store.subscribe(self.update)
        self.update(store.state)

    def update(self, state):
        if state["appMode"] == AppModes.ARMED:
            LCD.write(0, 0, "Armed           ")
            return

        if state["appMode"] == AppModes.DISARMED:
            LCD.write(0, 0, "Disarmed        ")
            return

        LCD.write(0, 0, "                ")

    def clear(self):
        self.__lcd.clear()
