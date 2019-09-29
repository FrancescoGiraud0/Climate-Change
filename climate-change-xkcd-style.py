import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("1880-2019.csv",skiprows=4)

colors = ["r" if value>=0 else "b" for value in data["Value"]]


plt.figure()
plt.xkcd()

plt.title("Global Temperature Anomalies")

bargraph = plt.bar(data["Year"], data["Value"])

plt.yticks(np.arange(-0.5,0.95,0.1))

for i, color in enumerate(colors):
    bargraph[i].set_color(color)

plt.annotate('WE ARE\nHERE...', xy=(2019,0.92), arrowprops=dict(arrowstyle='->'), xytext=(1985,0.8))

plt.show()