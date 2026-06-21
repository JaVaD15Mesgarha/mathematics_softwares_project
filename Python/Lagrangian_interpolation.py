import numpy as np
from scipy.interpolate import lagrange, CubicSpline
from numpy.polynomial.polynomial import Polynomial

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([1, 3, 5, 8, 5, 2])

poly_lagrange = lagrange(x, y)
coefs = Polynomial(poly_lagrange.coef[::-1])
print(coefs)

cs = CubicSpline(x, y)
print(cs.c)
