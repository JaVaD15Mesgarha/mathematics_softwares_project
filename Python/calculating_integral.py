import numpy as np
from scipy.integrate import simpson, trapezoid, fixed_quad

def f(x):
    return np.exp(x**2)

x_vals = np.linspace(0, 1, 200)
y_vals = f(x_vals)

trap_result = trapezoid(y_vals, x_vals)
simp_result = simpson(y_vals, x=x_vals)

print(f"Integral using Trapezoidal rule: {trap_result}")
print(f"Integral using Simpson's rule: {simp_result}")

#guass integral
gauss_result, _ = fixed_quad(f, 0, 1, n=5)
print(f"Integral using Gaussian Quadrature (n=5): {gauss_result}")