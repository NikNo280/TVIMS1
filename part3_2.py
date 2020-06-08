import matplotlib.pyplot as plt
import numpy as np
import math
from creature_Y import get_Y, empiric_func


n = 30
Y = get_Y(n)
print("Вариационный ряд: ")
print(Y)
fig, ax = plt.subplots(1, 1, figsize=(16, 9))
y = empiric_func(Y)
plt.step(Y, y, color='r', label='Эмпирическая функция распределения')
plt.plot([-1.5, Y[0]], [0, 0], color='r')
plt.plot([Y[-1], 1.5], [1, 1], color='r')
plt.plot([Y[0], Y[0]], [0, y[1]], color='r')


y_theoretical = list()
for yi in Y:
    y_theoretical.append((yi ** 3 + 1) / 2)
x_theoretical = np.linspace(-1, 1, 1000)
plt.plot(x_theoretical, (x_theoretical ** 3 + 1) / 2, color='blue', label='Теоретическая функция распределения')
plt.legend()


d_plus = []
d_minus = []
for i in range(0, n):
    d_plus.append((i / n) - ((Y[i]) ** 3 + 1) / 2)
    d_minus.append((((Y[i]) ** 3 + 1) / 2) - ((i - 1) / n))


my_lambda = (n ** 0.5) * max(max(d_plus), max(d_minus))
table_lambda = 1.36 # a = 0.05


if my_lambda > table_lambda:
    print(my_lambda.__str__() + " > " + table_lambda.__str__() + "\nСледовательно: ")
    print("Выборка не соответствует теоретическому закону распределения по критерию Колмогорова")
else:
    print(my_lambda.__str__() + " < " + table_lambda.__str__() + "\nСледовательно: ")
    print("Выборка соответствует теоретическому закону распределения по критерию Колмогорова")
plt.show()
plt.show()