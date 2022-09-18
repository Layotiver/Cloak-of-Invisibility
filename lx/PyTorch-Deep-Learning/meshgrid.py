import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,500,30)
print("x的维度:{},shape:{}".format(x.ndim, x.shape))
print(x)
y = np.linspace(0,500,20)
print("y的维度:{},shape:{}".format(y.ndim, y.shape))
print(y)

xv,yv = np.meshgrid(x, y)
print("xv的维度:{},shape:{}".format(xv.ndim, xv.shape))
print("yv的维度:{},shape:{}".format(yv.ndim, yv.shape))

plt.plot(xv, yv, '.')
plt.grid(True)
plt.show()
