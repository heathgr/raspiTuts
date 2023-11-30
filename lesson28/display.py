from LCD import LCD


class Display:
    def __init__(self):
        self.__lcd = LCD(2, 0x27, True)

    def subscribe(self, store):
        store.subscribe(self.update)
        self.update(store.state)

    def update(self, state):
        isEditableMessage = "set" if state["isEditable"] else "armed"
        aboveMessage = "<" if state["triggerLessThan"] else ">"

        self.__lcd.message(f"temp: {state['temp']} F", 1)
        self.__lcd.message(
            f"{isEditableMessage} {aboveMessage} {state['triggerPoint']}.", 2)

    def clear(self):
        self.__lcd.clear()
