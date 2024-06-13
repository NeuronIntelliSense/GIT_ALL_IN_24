import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def relu(x):
    if x <= 0:
        return 0
    else:
        return x


def elu(x, alpha=0.01):
    if x <= 0:
        return alpha * (math.exp(x) - 1)
    else:
        return x


def is_number(n):
    try:
        float(n)

    except ValueError:
        return False
    return True


def exercise2():
    n = input("Input x = ")

    if is_number(n):
        n = float(n)
        func = input("Input activation function (sigmoid|relu|elu): ")
        if func.lower() == "sigmoid":
            print(f"sigmoid: f({n}) = {sigmoid(x=n):.5f}")
        elif func.lower == "relu":
            print(f"ReLU: f({n}) = {relu(x=n):.5f}")
        elif func.lower == "elu":
            print(f"ELU: f({n}) = {elu(x=n):.5f}")
        else:
            print(f"{func} is not supported")
    else:
        print("x must be a number.")
