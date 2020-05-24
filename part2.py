import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable
from creature_Y import creature_Y
np.random.seed(666)

n = 10000
eps = n ** -1
Y = creature_Y(n)
print("Вариационный ряд: ")
print(Y)
sum_min8_min4 = 0
sum_min4_14 = 0
sum_14_28 = 0
M = int(n ** 0.5)
for i in Y:
    if i == -4:
        sum_min8_min4 += 0.5
        sum_min4_14 += 0.5
    elif i == 14:
        sum_min4_14 += 0.5
        sum_14_28 += 0.5
    elif i >= -8 and i < -4:
        sum_min8_min4 += 1
    elif i > -4 and i < 14:
        sum_min4_14 += 1
    elif i > 14 and i <= 28:
        sum_14_28 += 1
th = ['Значение', 'Количество']
td = ['[-8, -4)', sum_min8_min4,
      '(-4, 14)', sum_min4_14,
      '(14, 28]', sum_14_28]
columns = 2
table = PrettyTable(th)
td_data = td[:]
while td_data:
    table.add_row(td_data[:columns])
    td_data = td_data[columns:]
print(table)

# График
fig, ax = plt.subplots(4, 1, figsize=(16, 9))

fig.set_facecolor('floralwhite')
h = (Y[-1] - Y[0]) / M
A = Y[0]
B = A + h
temp_sum_1 = 0
temp_sum_2 = 0
poligon_point = list()
poligon_h = list()

for i in Y:
    if A <= i and i < B:
        temp_sum_1 += 1
    elif i == B and i != 28:
        temp_sum_1 += 0.5
        temp_sum_2 += 0.5
    elif i == B and i == 28:
        temp_sum_1 += 1
    elif i > B:
        ax[0].bar((A + B) / 2, temp_sum_1 / n, width=h)
        poligon_point.append((A + B) / 2)
        poligon_h.append(temp_sum_1 / n)
        temp_sum_1 = temp_sum_2
        temp_sum_2 += 0
        if A <= i and i < B + eps:
            temp_sum_1 += 1
        if i == B:
            temp_sum_1 += 0.5
            temp_sum_2 += 0.5
        A = B
        B += h
        B = round(B, 8)
ax[0].bar((A + B) / 2, temp_sum_1 / n, width=h)
poligon_point.append((A + B) / 2)
poligon_h.append(temp_sum_1 / n)
ax[0].plot(poligon_point, poligon_h, color='black')

m = int(n / 4)
poligon_point_2 = list()
poligon_h_2 = list()
for i in range(0, 4):
    if i == 0:
        ax[1].bar((Y[(i+1)*m - 1] + Y[i*m]) / 2, m /(n * (Y[(i+1)*m - 1] - Y[i*m])), width=Y[(i+1)*m - 1] - Y[i*m])
        poligon_point_2.append((Y[(i+1)*m - 1] + Y[i*m]) / 2)
        poligon_h_2.append(m /(n * (Y[(i+1)*m - 1] - Y[i*m])))
    else:
        ax[1].bar((Y[(i + 1) * m - 1] + Y[i * m - 1]) / 2, m / (n * (Y[(i + 1) * m - 1] - Y[i * m])), width=Y[(i + 1) * m - 1] - Y[i * m])
        poligon_point_2.append((Y[(i + 1) * m - 1] + Y[i * m - 1]) / 2)
        poligon_h_2.append(m / (n * (Y[(i + 1) * m - 1] - Y[i * m - 1])))

counts_empirically, bins_empirically = np.histogram(Y, bins=n)
cdf = np.cumsum(counts_empirically / n)
ax[2].plot(bins_empirically[1:], cdf)
ax[2].plot([-8, 28], [6/30, 24/30], 'r', [28, 30], [1, 1], color='r')
ax[2].plot([-10, -8], [0, 0], 'r', [-8], [0], 'o', color='r')
ax[2].plot([28], [24/30], 'o', color='r')
ax[1].plot(poligon_point_2, poligon_h_2, color='black')

ax[3].plot([-8, -8, 28, 28], [1/5, 1/60, 1/60, 1/5])
ax[3].plot(poligon_point, poligon_h, color='black')
plt.show()