import time
import datetime

class Item:
    def __init__(self, number: int):
        self._number = number

    @property
    def num(self):
        return self._number

    def time(self):
        return datetime.time.second - self.num


print("test")
