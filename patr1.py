import matplotlib.pyplot as plt
import numpy as np
np.random.seed(666)

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

n = 100
Mx = 5
Dx = 75
c = 1/30
b = 20
a = -10

summin2 = 0
sum2 = 0
summid = 0
Y = creature_Y(n)
for i in Y:
    if i == -2:
        summin2 += 1
    elif i == 2:
        sum2 += 1
    else:
        summid += 1

print("Количество -2 = " + summin2.__str__())
print("Количество центральных элементов = " + summid.__str__())
print("Количество 2 = " + sum2.__str__())

print(Y)

fig, ax1,  = plt.subplots(figsize=(16, 9))
counts_empirically, bins_empirically = np.histogram(Y, bins=n)
cdf = np.cumsum(counts_empirically / n)
ax1.plot(bins_empirically[1:], cdf)
ax1.set_title('Эмпирическая и теоретическая функции распределения')
ax1.set_ylabel('P')
ax1.set_xlabel('F(x)')
ax1.plot([-2, 2, 2], [9/30, 11/30, 1])
fig.tight_layout()
plt.show()

