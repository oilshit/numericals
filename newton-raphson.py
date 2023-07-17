# Newton-Raphson method
## used to get the root approximation of the
## real-valued function (wikipedia.org)

import math
import matplotlib.pyplot as plt

def f(x):
    """
    define the y as a function of x
    let say f(x) = e^x - 5x^2
    """

    return math.exp(x) - (5 * (x ** 2))

def diff_f(x):
    """
    define the differential or derivative of y
    as a function of x
    in case of y = f(x) = e^x - 5x^2, dy/dx = e^x - 10x
    """

    return math.exp(x) - (10 * x)

def newton_raphson(x, fx, dfx):
    """
    Newton-Raphson method
    will be get the new x according to the slope
    of the differencial function
    """
    
    return x - (fx / dfx)

iter = 0
epsilon = 1E-15
x0 = 1

x = [i * 0.01 for i in range(-100, 100 + 1)]
y = [f(i * 0.01) for i in range(-100, 100 + 1)]

plt.plot(x, y, label="f(x) = e^x - 5x^2")

while (True):
    dfx = (f(x0 + 1E-10) - f(x0)) / 1E-10
    x1 = newton_raphson(x0, f(x0), dfx)

    if (abs(x1 - x0) < epsilon):
        break
    
    iter += 1
    plt.plot([x0, x1], [f(x0), 0], label=("iter " + str(iter)))
    x0 = x1
    plt.plot([x0, x0], [0, f(x0)], linestyle="dashed", color="black")

print("x =", round(x0, 6), "with", iter, "iterations")
print("Newton-Raphson iteration plotted")

plt.title("Newton-Raphson Method\nfor e^x - 5x^2")
plt.xlabel("x")
plt.xlim(0, 1)
plt.ylim(0, f(1))
plt.ylabel("y = f(x)")

plt.scatter(x0, f(x0), label=("x found: " + str(round(x0, 6))))

plt.legend()

plt.show()
# plt.savefig("newton-raphson-result.png")