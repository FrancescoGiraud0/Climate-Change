import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("1880-2017.csv",skiprows=4)

colors = ["r" if value>=0 else "b" for value in data["Value"]]

bargraph = plt.bar(data["Year"], data["Value"])

for i, color in enumerate(colors):
    bargraph[i].set_color(color)

plt.show()
