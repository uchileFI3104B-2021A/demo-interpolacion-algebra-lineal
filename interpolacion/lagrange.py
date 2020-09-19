import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

x = np.array([1, 3, 7, 9])
y = np.array([2, 4, 1, 2])

lagrange_poly = lagrange(x, y)
x_to_plot = np.linspace(1, 9, 50)

plt.clf()
plt.plot(x, y, 'x', ms=12)
plt.plot(x_to_plot, lagrange_poly(x_to_plot), label='Lagrange')
plt.plot([5], lagrange_poly([5]), 'o', ms=15)

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()