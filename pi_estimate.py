#!/usr/bin/python3

import random
import matplotlib.pyplot as plt

SAVE_FILENAME = "assets/images/pi_estimate.png"
# TITLE = "Pi Estimation"
X_LABEL = "X"
Y_LABEL = "Y"
N = 10000
n_in = []
n_out = []

for point in range(N):
    x, y = (random.random(), random.random())
    if x * x + y * y <= 1.:
        n_in.append((x, y))
    else:
        n_out.append((x, y))

num_n_in = len(n_in)
num_n_out = len(n_out)
num_n_tot = num_n_in + num_n_out
est_pi = 4. * float(num_n_in) / float(num_n_tot)

print("Number of points inside the circle(n_in) : ", num_n_in)
print("Number of points outside the circle(n_out) : ", num_n_out)
print("Estimated pi = 4*n_in/n_tot(n_in + n_out) : ", est_pi)

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 10))
x_n_in = [x[0] for x in n_in]
y_n_in = [y[1] for y in n_in]
x_n_out = [x[0] for x in n_out]
y_n_out = [y[1] for y in n_out]
ax.plot(x_n_in, y_n_in, marker=".", lw=0, c="blue")
ax.plot(x_n_out, y_n_out, marker=".", lw=0, c="red")
ax.legend(["Num. of n_in : {}".format(num_n_in), "Num. of n_out : {}".format(num_n_out)])
ax.set_title("Total N : {}, Estimated Pi : {}".format(num_n_tot, est_pi), fontsize=20)
ax.set_xlabel(X_LABEL, fontsize=14)
ax.set_ylabel(Y_LABEL, fontsize=14)
circle = plt.Circle((0, 0), 1, color='gray', alpha=0.4)
fig.gca().add_artist(circle)
fig.savefig(SAVE_FILENAME)
plt.show()
