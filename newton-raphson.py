# Newton-Raphson method
## used to get the root approximation of the
## real-valued function (wikipedia.org)

import time

import matplotlib.pyplot as plt

def f(x):
    """
    define the y as a function of x
    let say f(x) = x^2 - 6x - 16
    """

    return (x**2) - 6 * x - 16

def diff_f(x):
    """
    define the differential or derivative of y
    as a function of x
    in case of y = f(x) = x^2 - 6x - 16, dy/dx = 2x - 6
    """

    return 2 * x - 6

def newton_raphson(x, fx, dfx):
    """
    Newton-Raphson method
    will be get the new x according to the slope
    of the differencial function
    """
    
    return x - (fx / dfx)

iter = 0
epsilon = 0.000000001
x0 = 25

x = [i * 0.25 for i in range(-25, 100 + 1)]
y = [f(i * 0.25) for i in range(-25, 100 + 1)]

plt.plot(x, y, label="f(x) = x^2 - 6x - 16")

while (True):
    x1 = newton_raphson(x0, f(x0), diff_f(x0))

    if (abs(x1 - x0) < epsilon):
        break
    
    iter += 1
    plt.plot([x0, x1], [f(x0), 0], label=("iter " + str(iter)))
    x0 = x1
    
    # print(x0)
    # time.sleep(1)

print("x =", round(x0, 2), "with", iter, "iterations")
print("Newton-Raphson iteration plotted")

plt.title("Newton-Raphson Method\nfor x^2 - 6x - 16")
plt.xlabel("x")
plt.xlim(0, 25)
plt.ylim(0, f(25))
plt.ylabel("y = f(x)")

plt.scatter(x0, f(x0), label=("x found: " + str(round(x0, 2))))

plt.legend()

# plt.show()
plt.savefig("newton-raphson-result.png")