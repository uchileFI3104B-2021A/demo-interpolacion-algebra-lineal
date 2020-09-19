import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, CubicSpline


def runge(x):
    return 1 / (1 + 25 * x**2)


x = np.linspace(-1, 1, 11)
y = runge(x)

x_to_plot = np.linspace(-1, 1, 100)
lagrange_poly = lagrange(x, y)
spline = CubicSpline(x, y, bc_type='natural')

plt.clf()
plt.plot(x, y, 'x', ms=15)
plt.plot(x_to_plot, runge(x_to_plot), label='Runge')
plt.plot(x_to_plot, lagrange_poly(x_to_plot), label='Lagrange')
plt.plot(x_to_plot, spline(x_to_plot), label='Spline Natural')


plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()