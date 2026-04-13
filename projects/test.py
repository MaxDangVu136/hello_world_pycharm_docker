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
Z = np.zeros(shape=X.shape)

print("========\n2. Testing Matplotlib...")
root_idxs = np.where(Y == 0)[0]
plt.plot(X, Y)
plt.scatter(
    X[root_idxs], Y[root_idxs], zorder=20,
    marker='*', c='k', label='Roots'
)
plt.axhline(
    y=0, linestyle="--",
    color='red', label='$Y = 0$'
)

plt.grid()
plt.xlim([np.min(X), np.max(X)])
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
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

plotter = pv.Plotter()
plotter.add_points(
    points=np.vstack((X, Y, Z)).T,
    render_points_as_spheres=True,
    color='green', label='Y = X^2 - 10X + 21'
)
plotter.add_axes()
plotter.add_legend(bcolor=None)
plotter.show()

print("Pyvista plotted.")
