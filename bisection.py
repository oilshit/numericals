import math
import matplotlib.pyplot as plt

def f(x):
    return math.exp(x) - (5 * (x ** 2))

x = [i * 0.05 for i in range(-50, 50 + 1)]
y = [f(i * 0.05) for i in range(-50, 50 + 1)]

plt.plot(x, y, label="f(x) = e^x - 5x^2")

def bisection(a, b, eps):
    a, b = a, b
    iter = 0

    while (abs(a - b) >= eps):
        c = (a + b) / 2
        fa, fc = f(a), f(c)

        if (fa * fc < 0):
            b = c

        else:
            a = c

        iter += 1

    return c, iter

def bisection_plot(a, b, eps) -> None:
    a, b = a, b
    iter = 0

    plt.xlim(-1 * abs((a - b) / 2), abs(a - b))
    plt.ylim(f(abs(a - b)) * -1, f(abs(a - b)))

    plt.plot([a, a], [0, f(a)], color="black", linestyle="dashed")
    plt.plot([b, b], [0, f(b)], color="black", linestyle="dashed")

    while (abs(a - b) >= eps):
        c = (a + b) / 2
        fa, fc = f(a), f(c)

        plt.plot(
            [c, c], [0, f(c)],
            color="black",
            linestyle="dashed",
            label=("iter " + str(iter))
        )

        if (fa * fc < 0):
            b = c

        else:
            a = c

        iter += 1

    plt.grid()
    plt.xlabel("x")
    plt.ylabel("y = f(x)")

    plt.scatter(c, f(c), color="orange", label="solution")

    plt.show()

    return

a, b = 0, 1
eps = 0.00001
eps2 = 0.000001

solution, iter = bisection(a, b, eps)
print("Using bisection method, solution of e^x - 5x^2 =",
      round(solution, 6),
      "with", iter, "iterations")

bisection_plot(a, b, eps)