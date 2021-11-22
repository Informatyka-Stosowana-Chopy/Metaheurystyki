import pandas as pd


class Reader:

    @staticmethod
    def read_csv():
        df = pd.read_csv("../data/dane.csv", sep=';')
        return df
