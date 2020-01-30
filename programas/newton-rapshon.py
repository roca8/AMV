def f(x):
    return (x - 3) * (x - 2) * (x - 1)


def fp(x):
    return 3 * x ** 2 - 12 * x + 11


def nr(x):
    print(x)
    if abs(f(x)) >= 0.000001:
        nr(x - f(x) / fp(x))
    else:
        return x


if __name__ == '__main__':
    nr(10)
