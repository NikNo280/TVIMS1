import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable
from creature_Y import creature_Y
np.random.seed(666)

n = 10000
eps = n ** -1
Y = creature_Y(n)

sum_mintwo_minone = 0
sum_minone_zero = 0
sum_zero_one = 0
sum_one_two = 0
M = int(n ** 0.5)
for i in Y:
    if i == -1:
        sum_mintwo_minone += 0.5
        sum_minone_zero += 0.5
    elif i == 0:
        sum_minone_zero += 0.5
        sum_zero_one += 0.5
    elif i == 1:
        sum_zero_one += 0.5
        sum_one_two += 0.5
    elif i >= -2 and i < -1:
        sum_mintwo_minone += 1
    elif i > -1 and i < 0:
        sum_minone_zero += 1
    elif i > 0 and i < 1:
        sum_zero_one += 1
    elif i > 1 and i <= 2:
        sum_one_two += 1

th = ['Значение', 'Количество']
td = ['[-2, -1)', sum_mintwo_minone,
      '(-1, 0)', sum_minone_zero,
      '(0, 1)', sum_zero_one,
      '(1, 2]', sum_one_two]
columns = 2
table = PrettyTable(th)
td_data = td[:]
while td_data:
    table.add_row(td_data[:columns])
    td_data = td_data[columns:]
print(table)

# График

x1 = np.arange(-2, -1.9)
y1 = np.random.randint(1, 20, size = 7)
x2 = np.arange(1, 101)
y2 = np.random.randint(1, 20, size = 100)

fig, ax = plt.subplots(3, 1, figsize=(16, 9))

fig.set_facecolor('floralwhite')
h = (Y[-1] - Y[0]) / M
A = Y[0]
B = A + h
temp_sum = 0
for _ in range(0, M):
    for y in Y:
        if A <= y and y <= B + eps:
            temp_sum += 1
    ax[0].bar((A + B) / 2, temp_sum/n, width=h)
    temp_sum = 0
    A = B
    B += h

m = int(n / 4)
for i in range(0, 3):
    ax[1].bar((Y[(i+1)*m] + Y[i*m]) / 2, m /(n * (Y[(i+1)*m] - Y[i*m])), width=Y[(i+1)*m] - Y[i*m])
ax[1].bar((Y[n - 1] + Y[7499]) / 2, m /(n * (Y[n - 1] - Y[7499])), width=Y[n - 1] - Y[7499])

counts_empirically, bins_empirically = np.histogram(Y, bins=n)
cdf = np.cumsum(counts_empirically / n)
ax[2].plot(bins_empirically[1:], cdf)
ax[2].plot([-8, 14, 28, 28], [6/30, 17/30, 24/30, 1])

plt.show()