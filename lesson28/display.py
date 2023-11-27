from LCD import LCD


class Display:
    def __init__(self):
        self.__lcd = LCD(2, 0x27, True)

    def register(self, store):
        store.subscribe(self.update)

    def update(self, state):
        aboveMessage = "below" if state["triggerLessThan"] else "above"

        self.__lcd.message(f"Temp: {state['tempurature']}", 1)
        self.__lcd.message(
            f"Alarm when {aboveMessage} {state['triggerPoint']}.")
