import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable
from creature_Y import creature_Y
np.random.seed(666)

n = 100000
Y = creature_Y(n)
sum_mintwo_minone = 0
sum_minone_zero = 0
sum_zero_one = 0
sum_one_two = 0

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

fig, ax = plt.subplots(2, 1, figsize=(16, 9))

fig.set_facecolor('floralwhite')
ax[0].bar(-1.5, sum_mintwo_minone, width=1)
ax[0].bar(-0.5, sum_minone_zero, width=1)
ax[0].bar(0.5, sum_zero_one, width=1)
ax[0].bar(1.5, sum_one_two, width=1)
ax[0].plot([-1.5, -0.5, 0.5, 1.5], [sum_mintwo_minone, sum_minone_zero, sum_zero_one, sum_one_two], color='black')

counts_empirically, bins_empirically = np.histogram(Y, bins=n)
cdf = np.cumsum(counts_empirically / n)
ax[1].plot(bins_empirically[1:], cdf)
ax[1].plot([-2, 2, 2], [9/30, 11/30, 1])

plt.show()