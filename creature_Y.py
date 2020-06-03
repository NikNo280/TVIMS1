import numpy as np

b = 1
a = -1

def get_Y(n):
    ksi = list(np.random.random() for _ in range(n))
    X = list(map(lambda ksi: ksi * (b - a) + a, ksi))
    Y = list()
    for xi in X:
        if xi < 0:
            Y.append(-(abs(xi) ** (1 / 3)))
        else:
            Y.append(xi ** (1 / 3))
    return sorted(Y)


def empiric_func(Y):
    F_y = list()
    h = 0
    for yi in Y:
        h += Y.count(yi)/len(Y)
        F_y.append(h)
    return F_y





