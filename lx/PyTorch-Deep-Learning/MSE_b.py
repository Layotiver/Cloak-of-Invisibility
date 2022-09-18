import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

def forward(x):
    return w * x + b

# Training Loss
def loss(x, y):
    y_pred = forward(x)
    return (y_pred - y) * (y_pred - y)


mse_b_list = []
W = np.arange(0.0, 4.1, 0.1)
B = np.arange(0.0, 4.1, 0.1)
[w,b] = np.meshgrid(W,B)

l_sum = 0
for x_val, y_val in zip(x_data, y_data):
    l_sum += loss(x_val, y_val)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(w,b,l_sum/3)
plt.show()