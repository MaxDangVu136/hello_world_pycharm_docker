import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import sys

print("Hello World from Docker!")
print("This is the test.py file.")
print("The current version of Python is:", sys.version)

print("Identity is:\n", np.eye(3))

X = np.arange(0, 11, 1)
Y = X**2 - 10*X + 21

plt.scatter(X, Y)
plt.xlabel('X')
plt.ylabel('Y')
plt.axhline(y=0, color='red')
plt.title('2X + 1 (testing matplotlib)')
plt.show()
