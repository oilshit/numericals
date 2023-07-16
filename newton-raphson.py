# Newton-Raphson method
## used to get the root approximation of the
## real-valued function (wikipedia.org)

import time

def f(x: int | float):
    """
    define the y as a function of x
    let say f(x) = x^2 + 4x - 32
    """

    return x**2 + 4 * x - 32

def diff_f(x: int | float):
    """
    define the differential or derivative of y
    as a function of x
    in case of y = f(x) = x^2 + 4x - 32, dy/dx = 2x + 4
    """

    return 2 * x + 4

def newton_raphson(x: int | float, fx: int | float, dfx: int | float):
    """
    Newton-Raphson method
    will be get the new x according to the slope
    of the differencial function
    """
    
    return x - (fx / dfx)

iter = 0
epsilon = 0.000000001
x0 = 10

while (True):
    x1 = newton_raphson(x0, f(x0), diff_f(x0))

    if (abs(x1 - x0) < epsilon):
        break
    
    iter += 1
    x0 = x1
    
    # print(x0)
    # time.sleep(1)

print("x =", round(x0, 2), "with", iter, "iterations")
