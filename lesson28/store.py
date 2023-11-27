from itertools import chain


class Store:
    callbacks = []
    __state = None

    def __init__(self, initial_state):
        self.__state = initial_state

    def subscribe(self, callback):
        self.callbacks.append(callback)

    def update(self, newState):
        self.__state = dict(chain(self.__state.items(), newState.items()))
        for callback in self.callbacks:
            callback(self.__state)
