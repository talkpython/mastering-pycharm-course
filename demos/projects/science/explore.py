import numpy as np
import matplotlib.pyplot as plt

N = 50
x = np.random.random(N)
y = np.random.random(N)
colors = np.random.random(N)

area = np.pi * (15 * np.random.random(N))

plt.scatter(x, y, s=area, alpha=.5)
plt.show()

input("Waiting for exit...")
