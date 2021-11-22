import pandas as pd


class Items:

    def __init__(self):
        self.all_items = self.read_csv()

    @staticmethod
    def read_csv():
        df = pd.read_csv("data/dane.csv", sep=';')
        return df
