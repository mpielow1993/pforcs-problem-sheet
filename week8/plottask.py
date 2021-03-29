# Reference: https://www.w3resource.com/graphics/matplotlib/basic/matplotlib-basic-exercise-5.php
# Reference: https://matplotlib.org/2.0.2/users/mathtext.html
# Reference: https://stackoverflow.com/questions/477486/how-to-use-a-decimal-range-step-value

import numpy as np
import matplotlib.pyplot as plt

# Method:   plot_functions()
# Description:  Outpus a plot of three functions defined within the method body.
def plot_functions():
    x_points = np.array(np.arange(0.0, 4.0, 0.1))
    f_points = x_points
    g_points = x_points * x_points
    h_points = x_points * x_points * x_points
    plt.plot(x_points, f_points, label = r'$f(x) = x$')
    plt.plot(x_points, g_points, label = r'$g(x) = x^2$')
    plt.plot(x_points, h_points, label = r'$h(x) = x^3$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('G00398780 - Weekly Task 08')
    plt.legend()
    plt.show()
