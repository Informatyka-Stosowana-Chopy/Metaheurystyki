from items import Items


class Backpack:
    def __init__(self, max_capacity: int):
        self.max_capacity = max_capacity
        self.items = Items.read_csv()
