import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10000, 400)
y = np.cbrt(x) - 2

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
