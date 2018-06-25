#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

FILEPATH = "assets/"
FILENAME = "647_Global_Temperature_Data_File.txt"
TITLE = "Global Temperature"
X_LABEL = "YEAR"
Y_LABEL = "Temperature Anomaly (C)"

coll_name = ["Year", "1-year Mean", "5-year Mean"]
df = pd.read_csv(FILEPATH+FILENAME, delimiter="\s+", header=None)
df.columns = coll_name

x = df[coll_name[0]]
y1 = df[coll_name[1]]
y2 = df[coll_name[2]]

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 5))
ax.plot(x, y1, c="blue", ls="-.", marker="o", ms="4", mec="blue", mfc="white", label=coll_name[1])
ax.plot(x, y2, c="black", ls="-", lw="5", label=coll_name[2])
plt.xticks(np.arange(1880, 2030, 10))
plt.yticks(np.arange(-0.5, 1.5, 0.5))
ax.legend()

ax.set_title(TITLE, fontsize=20)
ax.set_xlabel(X_LABEL, fontsize=14)
ax.set_ylabel(Y_LABEL, fontsize=14)
ax.grid(c="gray", ls="-", lw=2)
plt.show()
