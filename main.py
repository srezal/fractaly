import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')
x = np.arange(-10, 10.01, 0.01)
plt.plot(x, x**2)
plt.show()