import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate
from creature_Y import creature_Y
np.random.seed(666)

n = 20
Y = creature_Y(n)
print("Вариационный ряд: ")
print(Y)

My = sum(Y) / n
print('My = ', My)

Dy = 0
for y in Y:
    Dy += (y - My) ** 2
Dy = Dy / (n - 1)
print('Dy = ', Dy)

T = [1.73, 2.093, 2.861] #significance level 0.9 0.95 0.99
intervals = []
for t in T:
    intervals.append((My - np.sqrt(Dy) * t / np.sqrt(n - 1), My + np.sqrt(Dy) * t / np.sqrt(n - 1)))

print(intervals)

gamma = [0.9, 0.95, 0.99]
plt.plot(gamma, [interval[1] - interval[0] for interval in intervals])
plt.xlabel("$\gamma$")
plt.ylabel("Interval value")
plt.show()
#todo
Disp_teor = integrate.quad(lambda x: (x ** 4)/2, -(4)**(1/3), 2**(1/3))[0] - \
(integrate.quad(lambda x: (x ** 3)/2, -(4)**(1/3), 2**(1/3)))[0]**2
print("D (theoretical) = ", Disp_teor)

intervals2 = []
for t in T:
    intervals2.append((My - np.sqrt(Disp_teor) * t / np.sqrt(n - 1), My + np.sqrt(Disp_teor) * t / np.sqrt(n - 1)))
print(intervals2)
plt.plot(gamma, [interval[1] - interval[0] for interval in intervals2])
plt.xlabel("$\gamma$")
plt.ylabel("Interval value")
plt.show()