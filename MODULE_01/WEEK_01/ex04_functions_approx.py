import math

x_cond = 'x must be radian'
n_cond_int = 'n must be integer'
n_cond_zero = 'n must be greater than 0'


def factorial(n):
    factor = 1
    for i in range(1, n + 1):
        factor = factor * i

    return factor


def is_number(n):
    try:
        float(n)

    except ValueError:
        return False
    return True


def approx_sin(x, n):
    if not is_number(x):
        print(x_cond)
        return

    if not isinstance(n, int):
        print(n_cond_int)
        return

    if n <= 0:
        print(n_cond_zero)
        return

    x = float(x)

    result = 0
    for i in range(n):
        result += ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)

    print(result)


def approx_cos(x, n):
    if not is_number(x):
        print(x_cond)
        return

    if not isinstance(n, int):
        print(n_cond_int)
        return

    if n <= 0:
        print(n_cond_zero)
        return

    x = float(x)

    result = 0
    for i in range(n):
        result += ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)

    print(result)


def approx_sinh(x, n):
    if not is_number(x):
        print(x_cond)
        return

    if not isinstance(n, int):
        print(n_cond_int)
        return

    if n <= 0:
        print(n_cond_zero)
        return

    x = float(x)

    result = 0
    for i in range(n):
        result += (x ** (2 * i + 1)) / factorial(2 * i + 1)

    print(result)


def approx_cosh(x, n):
    if not is_number(x):
        print(x_cond)
        return

    if not isinstance(n, int):
        print(n_cond_int)
        return

    if n <= 0:
        print(n_cond_zero)
        return

    x = float(x)

    result = 0
    for i in range(n):
        result += (x ** (2 * i)) / factorial(2 * i)

    print(result)
