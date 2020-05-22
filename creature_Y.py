import numpy as np

b = 20
a = -10

def creature_Y(n):
    ksi = list(np.random.random() for _ in range(n))
    X = list(map(lambda ksi: ksi * (b - a) + a, ksi))
    Y = list()
    for xi in X:
        if xi < -4:
            Y.append(-8)
        elif xi >= -4 and xi <= 14:
            Y.append(2 * xi)
        elif xi > 14:
            Y.append(28)
    return sorted(Y)