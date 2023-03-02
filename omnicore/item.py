import time


class Item():
    def __init__(self, number: int):
        self._number = number

    @property
    def num(self):
        return self._number


print("test")
