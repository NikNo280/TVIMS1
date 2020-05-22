import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable
from creature_Y import creature_Y
np.random.seed(666)

n = 10000
Y = creature_Y(n)

# Таблица данных
summin2 = 0
sum2 = 0
summid = 0

for i in Y:
    if i == -8:
        summin2 += 1
    elif i == 28:
        sum2 += 1
    else:
        summid += 1
th = ['Значение', 'Количество']
td = ['-8', summin2,
      '(-8, 28)', summid,
      '28', sum2]
columns = 2
table = PrettyTable(th)
td_data = td[:]
while td_data:
    table.add_row(td_data[:columns])
    td_data = td_data[columns:]
print(table)

# График
fig, ax1,  = plt.subplots(figsize=(16, 9))
counts_empirically, bins_empirically = np.histogram(Y, bins=n)
cdf = np.cumsum(counts_empirically / n)
ax1.plot(bins_empirically[1:], cdf)
ax1.set_title('Эмпирическая и теоретическая функции распределения')
ax1.set_ylabel('P')
ax1.set_xlabel('F(x)')
ax1.plot([-8, 14, 28, 28], [6/30, 17/30, 24/30, 1])
fig.tight_layout()  # убираем пустые места
ax1.grid()          # сетка
plt.axhline(0, color='black')
plt.show()



