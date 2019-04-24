# Program that solve the heat equation using finite differences

import heat
import test_function
# Factors
r = 0.3

dx = 0.1
dt = r*dx*dx
x_end = 3.
t_end = 6.
b = [0., 0.]
coef = 1.

# Creating and solving the problem
H = heat.Heat(dx, dt, x_end, t_end, coef, b, test_function.sinx)

H.heat_solve()

# Ploting the result using matplotlui
H.heat_plot()

