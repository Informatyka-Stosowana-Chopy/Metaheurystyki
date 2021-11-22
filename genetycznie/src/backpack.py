import pandas as pd

from reader import Reader


class Backpack:
    def __init__(self, max_capacity: int):
        self.max_capacity = max_capacity
        self.backpack = []
        self.all_items = Reader.read_csv()

    def roulette_wheel_selection(self):
        pass
