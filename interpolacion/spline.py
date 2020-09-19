import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline


x = np.array([1, 3, 7, 9])
y = np.array([2, 4, 1, 2])

spline = CubicSpline(x, y, bc_type='natural')
spline2 = CubicSpline(x, y, bc_type='clamped')
spline3 = CubicSpline(x, y, bc_type='not-a-knot')

x_to_plot = np.linspace(0, 10, 100)

plt.clf()
plt.plot(x, y, 'x', ms=12)
plt.plot(x_to_plot, spline(x_to_plot), label='Natural')
plt.plot(x_to_plot, spline2(x_to_plot), label='Clamped')
plt.plot(x_to_plot, spline3(x_to_plot), label='Not a Knot')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()