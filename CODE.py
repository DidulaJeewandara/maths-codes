# maths-codes
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 1000)
cos_4theta = np.cos(4*theta)
r = 2 * np.sqrt(np.clip(cos_4theta, 0, None))  #this is the angle

plt.polar(theta, r)
plt.title(r"$r = 2\sqrt{\cos(4\theta)}$")
plt.show()
