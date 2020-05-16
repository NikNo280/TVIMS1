import numpy as np

b = 20
a = -10

def creature_Y(n):
    ksi = list(np.random.random() for _ in range(n))
    X = list(map(lambda ksi: ksi * (b - a) + a, ksi))
    Y = list()
    for xi in X:
        if xi < -1:
            Y.append(-2)
        elif xi <= 1:
            Y.append(2 * xi)
        elif xi > 1:
            Y.append(2)
    return sorted(Y)