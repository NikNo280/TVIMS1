import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate
from creature_Y import get_Y
import scipy.stats as sts
np.random.seed(666)


D_theoretical = integrate.quad(lambda x: (x ** 2), -1, 1)[0] - \
                (integrate.quad(lambda x: x, -1, 1))[0]
print("D (theoretical) = ", D_theoretical)

gamma = [0.9, 0.95, 0.99]
N = [20, 30, 50, 70, 100, 150]

all_intervals = list()
for ni in N:
    intervals = []
    intervals2 = []
    T = []
    Y = get_Y(ni)
    print("Вариационный ряд: ")
    print(Y)

    My = sum(Y) / ni
    print('My = ', My)

    Dy = 0
    for y in Y:
        Dy += (y - My) ** 2
    Dy = Dy / (ni - 1)
    print('Dy = ', Dy)

    t_rv = sts.t(ni - 1)
    arr = t_rv.rvs(1000000)
    for i in gamma:
        tmp = sts.mstats.mquantiles(arr, prob=[1 - (1 - i) / 2])
        T.append(tmp[0])

    for ti in T:
        intervals.append((My - np.sqrt(Dy) * ti / np.sqrt(ni - 1),
                          My + np.sqrt(Dy) * ti / np.sqrt(ni - 1)))
        intervals2.append((My - np.sqrt(D_theoretical) * ti / np.sqrt(ni - 1),
                           My + np.sqrt(D_theoretical) * ti / np.sqrt(ni - 1)))
    print(intervals)
    print(intervals2)
    all_intervals.append(intervals2)
    plt.plot(gamma, [interval[1] - interval[0] for interval in intervals], color='r')
    plt.plot(gamma, [interval[1] - interval[0] for interval in intervals2], color='blue')
    title = 'n = ' + ni.__str__() + ' M = ' + My.__str__() + ' D = ' + Dy.__str__()
    plt.title(title)
    plt.show()

for i in range(0, 3):
    plt.plot(N, [(interval[i][1] - interval[i][0]) for interval in all_intervals])
    plt.show()