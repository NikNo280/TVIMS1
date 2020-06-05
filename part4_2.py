import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate
from creature_Y import get_Y
import scipy.stats as sts

gamma = [0.9, 0.95, 0.99]
N = [20, 30, 50, 70, 100, 150]
all_intervals = list()
M_theoretical = integrate.quad(lambda x: (x ** 3), -1, 1)[0]
print("M = ", M_theoretical)
for ni in N:
    intervals = []
    intervals2 = []
    Y = get_Y(ni)
    My = sum(Y) / ni
    print('My = ', My)

    Dy = 0
    for y in Y:
        Dy += (y - My) ** 2
    Dy = Dy / (ni - 1)
    print('Dy = ', Dy)
    D_theoretical = 0.
    for i in Y:
        D_theoretical += (i - M_theoretical) ** 2
    D_theoretical = D_theoretical / (ni - 1)

    chi_mass = sts.chi2(ni - 1)
    arr = chi_mass.rvs(100000)
    xi_plus = []
    xi_minus = []
    for i in gamma:
        temp = sts.mstats.mquantiles(arr, prob=[(1 - i) / 2, (1 + i) / 2])
        xi_plus.append(temp[0])
        xi_minus.append(temp[1])

    for i in range(3):
        intervals.append(((ni - 1) * Dy / xi_minus[i], (ni - 1) * Dy / xi_plus[i]))
    for i in range(3):
        intervals2.append((ni * D_theoretical / xi_minus[i], ni * D_theoretical / xi_plus[i]))
    all_intervals.append(intervals2)
    print(intervals)
    print(intervals2)
    plt.plot(gamma, [interval[1] - interval[0] for interval in intervals])
    plt.plot(gamma, [interval[1] - interval[0] for interval in intervals2])
    title = "n = " + ni.__str__()
    plt.title(title)
    plt.show()

print(all_intervals)
for i in range(0, 3):
    plt.plot(N, [(interval[i][1] - interval[i][0]) for interval in all_intervals])
    plt.show()