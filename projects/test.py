import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pyvista as pv

import sys

print("0. Prelude")
print("Hello World from Docker!")
print(f"This is the {__file__} file.")
print(f"Current Python version: {sys.version}.")

print("========\n1. Testing Numpy...")
print("Identity is:\n", np.eye(3))
X = np.arange(0, 11, 0.1)
Y = X**2 - 10*X + 21

print("========\n2. Testing Matplotlib...")
plt.plot(X, Y)
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim([0, np.max(X)])
plt.axhline(y=0, linestyle="--", color='red')
plt.title(r'$Y = X^2 - 10X + 21$')
plt.show()
print("Matplotlib plotted.")

print("========\n3. Testing PyVista...")
mesh = pv.Sphere()
plotter = pv.Plotter()
plotter.add_mesh(mesh)
plotter.add_axes()
plotter.add_title("Sphere Mesh")
plotter.show()
print("Pyvista plotted.")
