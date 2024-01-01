import LCD1602 as LCD
from appModes import AppModes


def maskInput(keypadInput):
    displayOutput = list(keypadInput)

    for i in range(len(displayOutput) - 2):
        displayOutput[i] = "*"

    return "".join(displayOutput).ljust(16)


class Display:
    def __init__(self):
        LCD.init(0X27, 1)

    def subscribe(self, store):
        store.subscribe(self.update)
        self.update(store.state)

    def update(self, state):
        appMode = state["appMode"]
        isArmed = state["isArmed"]
        armedStatus = "A" if isArmed else "D"

        if appMode == AppModes.ARMED:
            LCD.write(0, 0, f"Armed          {armedStatus}")
            return

        if appMode == AppModes.REQUEST_DISARM:
            LCD.write(0, 0, f"Enter password:{armedStatus}")
            LCD.write(0, 1, maskInput(state["keypadInput"]))
            return

        if appMode == AppModes.DISARMED:
            LCD.write(0, 0, f"Disarmed       {armedStatus}")
            return

        LCD.write(0, 0, f"               {armedStatus}")

    def clear(self):
        self.__lcd.clear()
