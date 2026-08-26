import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x**2) + (4*x) + 4

def df(x):
    return (2*x) + 4

def gradientDecent(starting_point, learning_rate, iterations):
    lX = []
    lY = []
    lf = []
    x = starting_point
    for i in range(iterations):
        lY.append(f(x))
        lX.append(i)
        x = x - learning_rate*df(x)
    return x, lX, lY

minimum, list_X, list_Y = gradientDecent(0, 0.1, 100)

print(minimum)
print(list)

plt.plot(list_X,list_Y,label="f(x)=x^2+4x+4")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Gradient Descent Visualization")
plt.legend()
plt.show()
