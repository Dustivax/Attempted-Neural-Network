%matplotlib inline
from matplotlib import pyplot as plt
import numpy as np
 

data = [[3, 1.5, 1], [2, 1, ,0], [4, 1.5, 1], [3, 1, 0], [3.5, .5, 1], [2, .5, 0], [5.5, 1, 1], [1, 1, 0]]
mystery_flower = [4.5, 1]

w1 = np.random.randn()
w2 = np.random.randn()
b = np.random.randn()

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def sigmoid_p(x):
    return sigmoid(x) * (1-sigmoid(x))

for i in range(1000):
    ri = np.random.randint(len(data))
    point = data[ri]
    print(point)

    z = point[0] * w1 + point[1] * w2 + b
    pred = sigmoid(z)

    target = point[2]
    cost = np.square(pred - target)

for i in range(len(data)):
    point = data[i]
    color = "r"
    if point[2] == 0:
        color = "b"
    plt.scatter(point[0], point[1], c = color)










#T = np.linespace(-5, 5, 100)
#Y = sigmiod(T)
#plt.plot(T, Y)
