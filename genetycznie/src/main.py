import pandas as pd

df = pd.read_csv("dane.csv", sep=';')

print(df['Waga'][0:4])