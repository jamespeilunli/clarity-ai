# make sure that that the csv is valid

import pandas as pd

df = pd.read_csv("out.csv")

print("info:")
print(df.info(), "\n" * 3)
print("head:")
print(df.head(), "\n" * 3)
