import numpy as np
import matplotlib.pyplot as plt
from pylab import *

x = np.arange(-5.0, 5.0, 0.02)
y1 = np.sin(x)

plt.figure(1)
plt.subplot(211)
plt.plot(x, y1)

plt.subplot(212)
#设置x轴范围
xlim(-2.5, 2.5)
#设置y轴范围
ylim(-1, 1)
plt.plot(x, y1)
