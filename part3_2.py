import matplotlib.pyplot as plt
import numpy as np
import math
from creature_Y import get_Y, empiric_func
np.random.seed(666)


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


x_theoretical = np.linspace(-1, 1, 30)
y_theoretical = (x_theoretical ** 3 + 1) / 2
plt.plot(x_theoretical, y_theoretical, color='blue', label='Теоретическая функция распределения')
plt.legend()


max = 0
for i in range(0, n):
    if max < math.fabs(y_theoretical[i] - y[i]):
       max = math.fabs(y_theoretical[i] - y[i])


table_lambda = 1.36 # a = 0.05
my_lambda = (n ** 0.5) * max


if my_lambda > table_lambda:
    print(my_lambda.__str__() + " > " + table_lambda.__str__() + "\nСледовательно: ")
    print("Выборка не соответствует теоретическому закону распределения по критерию Колмогорова")
else:
    print(my_lambda.__str__() + " < " + table_lambda.__str__() + "\nСледовательно: ")
    print("Выборка соответствует теоретическому закону распределения по критерию Колмогорова")
plt.show()
plt.show()