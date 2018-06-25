#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

FILEPATH = "assets/"
FILENAME = "co2_mm_mlo.txt"
TITLE = "Carbon Dioxide Measurement"
X_LABEL = "Time"
Y_LABEL = "CO2 (ppm)"

coll_name = ["year", "month", "decimal date", "average", "interpolated", "trend(season corr)", "days"]

df = pd.read_csv(FILEPATH+FILENAME, delimiter="\s+", skiprows=72, names=coll_name, header=None)

df_except = df[df["average"] != -99.99]
df_except_1_year_avr= df_except.groupby(['year'], as_index=False).mean()

x_monthly = df_except[coll_name[2]]
y_monthly = df_except[coll_name[3]]
x_annual = df_except_1_year_avr[coll_name[0]]
y_annual = df_except_1_year_avr[coll_name[3]]
#
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 5))
ax.plot(x_monthly, y_monthly, c="blue", ls="-.", marker="o", ms="4", mec="blue", mfc="white", label=coll_name[1])
ax.plot(x_annual, y_annual, c="black", ls="-", lw="4", label=coll_name[0])
# plt.xticks(np.arange(1880, 2030, 10))
# plt.yticks(np.arange(-0.5, 1.5, 0.5))
ax.legend()
ax.set_title(TITLE, fontsize=20)
ax.set_xlabel(X_LABEL, fontsize=14)
ax.set_ylabel(Y_LABEL, fontsize=14)
ax.grid(c="gray", ls="-", lw=2)
plt.show()
