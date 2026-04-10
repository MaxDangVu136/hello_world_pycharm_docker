import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pyvista as pv

import sys

print("Hello World from Docker!")
print("This is the test.py file.")
print("The current version of Python is:", sys.version)

print("Identity is:\n", np.eye(3))

X = np.arange(0, 11, 1)
Y = X**2 - 10*X + 21

print("Testing Matplotlib...")
plt.scatter(X, Y)
plt.xlabel('X')
plt.ylabel('Y')
plt.axhline(y=0, color='red')
plt.title(r'$X^2 - 10X + 21$')
plt.show()

print("Testing PyVista...")
mesh = pv.Sphere()
plotter = pv.Plotter()
plotter.add_mesh(mesh)
plotter.add_axes()
plotter.add_title("Sphere Mesh")
plotter.show()
