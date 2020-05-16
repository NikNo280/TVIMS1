import matplotlib.pyplot as plt
import numpy as np
np.random.seed(666)

n = 10000
Mx = 5
Dx = 75
c = 1/30
b = 20
a = -10
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
Y = sorted(Y)

summin2 = 0
sum2 = 0
summid = 0
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
print(ksi)
print(X)
print(Y)

fig, (ax1, ax2) = plt.subplots(
    nrows=1, ncols=2,
    figsize=(16, 9)
)
counts_empirically, bins_empirically = np.histogram(Y, bins=n)
cdf = np.cumsum(counts_empirically / n)
ax1.plot(bins_empirically[1:], cdf)
ax1.set_title('Эмпирическая функция распределения')
ax1.set_ylabel('P')
ax1.set_xlabel('F(x)')
fig.tight_layout()
plt.show()