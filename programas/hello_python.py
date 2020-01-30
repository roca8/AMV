import pandas as pd


def f(x):
    return (x - 3) * (x - 2) * (x - 1)


def fp(x):
    return 3 * x ** 2 - 12 * x + 11


if __name__ == '__main__':
    x0 = 10
    l = []
    i = 0
    arch = open('nr.txt', 'w')
    while abs(f(x0)) >= 0.000001:
        x0 = x0 - f(x0) / fp(x0)
        t = (i, x0, f(x0), fp(x0))
        arch.write(",".join(["%.6f" % x for x in t]))
        arch.write('\n')
        l.append(t)
        i += 1
    pd.DataFrame(l, columns=['i', 'x', 'f(x)', "f'(x)"]).to_excel('nr.xlsx', index=False)
    arch.close()

    print(u"Se encontró la raíz %.6f después de %d iteraciones" % (x0, i + 1))
