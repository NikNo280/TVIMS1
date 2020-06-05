import matplotlib.pyplot as plt
import numpy as np
from creature_Y import get_Y, empiric_func

n = 1521
Y = get_Y(n)
print("Вариационный ряд: ")
print(Y)

fig, ax = plt.subplots(4, 1, figsize=(16, 9))
fig.set_facecolor('floralwhite')



y = empiric_func(Y)
ax[0].step(Y, y, color='r', label='Эмпирическая функция распределения')
ax[0].plot([-1.5, Y[0]], [0, 0], color='r')
ax[0].plot([Y[-1], 1.5], [1, 1], color='r')
ax[0].plot([Y[0], Y[0]], [0, y[1]], color='r')

x_theoretical = np.linspace(-1, 1, 100)
y_theoretical = (x_theoretical ** 3 + 1) / 2
ax[0].plot(x_theoretical, y_theoretical, color='blue', label='Теоретическая функция распределения')
ax[0].legend()

if n <= 100:
    M = int(np.sqrt(n))
else:
    M = int(4 * np.log10(n))
h = (Y[-1] - Y[0]) / M
A = Y[0]
B = A + h
temp_sum_1 = 0
temp_sum_2 = 0
x_point = list()
f_y_h = list()
polygon_h = list()
for _ in range(0, M):
    for yi in Y:
        if A <= yi and yi < B:
            temp_sum_1 += 1
        elif yi == B:
            temp_sum_1 += 0.5
            temp_sum_2 += 0.5
    ax[1].bar((A + B) / 2, temp_sum_1 / (n * h), width=h)
    x_point.append((A + B) / 2)
    polygon_h.append(temp_sum_1 / n)
    f_y_h.append(temp_sum_1 / (h * n))
    temp_sum_1 = temp_sum_2
    temp_sum_2 = 0
    A = B
    B += h
    B = round(B, 8)
ax[1].plot(x_point, polygon_h, color='black')

# Delete random element
m = n // M
del_n = n - (M * m)
for _ in range(0, del_n):
    temp = np.random.choice(Y)
    Y.remove(temp)

x_point_2 = list()
polygon_h_2 = list()
A = np.zeros(M)
B = np.zeros(M)
A[0] = Y[0]
B[-1] = Y[-1]

for yi in range(1, M):
    A[yi] = (Y[m * yi] + Y[m * yi + 1]) / 2
    B[yi - 1] = A[yi]

for yi in range(M):
    ax[2].bar((A[yi] + B[yi]) / 2,
              m / (n * (B[yi] - A[yi])),
              width=B[yi] - A[yi])
    x_point_2.append((A[yi] + B[yi]) / 2)
    polygon_h_2.append(m / n)
ax[2].plot(x_point_2, polygon_h_2, color='black')
f_y = list()
for xi in x_theoretical:
    f_y.append(3/2*xi**2)
ax[3].plot(x_theoretical, f_y, color='blue', label='Теоретическая плотность распределения')
ax[3].plot(x_point, f_y_h, color='r', label='Эмпирическая плотность распределения')
ax[3].legend()
plt.show()

