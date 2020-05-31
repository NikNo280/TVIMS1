import matplotlib.pyplot as plt
import numpy as np
from creature_Y import get_Y
np.random.seed(666)


n = 200
if n <= 100:
    M = int(np.sqrt(n))
else:
    M = int(4 * np.log10(n))
Y = get_Y(n)

fig, ax = plt.subplots(1, 1, figsize=(16, 9))

h = (Y[-1] - Y[0]) / M
A = Y[0]
B = A + h
temp_sum_1 = 0
temp_sum_2 = 0
poligon_point = list()
poligon_h = list()

for yi in Y:
    if A <= yi and yi < B:
        temp_sum_1 += 1
    elif yi == B:
        temp_sum_1 += 0.5
        temp_sum_2 += 0.5
    else:
        plt.bar((A + B) / 2, temp_sum_1 / (n * h), width=h)
        poligon_point.append((A + B) / 2)
        poligon_h.append(temp_sum_1 / ( n * h))
        temp_sum_1 = temp_sum_2
        temp_sum_2 += 0
        A = B
        B += h
        B = round(B, 8)
        if A <= yi and yi < B:
            temp_sum_1 += 1
        if yi == B:
            temp_sum_1 += 0.5
            temp_sum_2 += 0.5
plt.plot(poligon_point, poligon_h, color='black')
x_theoretical = np.linspace(-1, 1, M)
f_y = list()
for xi in x_theoretical:
    f_y.append(3/2*xi**2)
plt.plot(x_theoretical, f_y, color='blue', label='Теоретическая плотность распределения')
plt.plot(poligon_point, poligon_h, color='r', label='Эмпирическая плотность распределения')


my_X_sqrt = 0
table_X_sqrt = 20.1 # a = 0,01 k = 8
f_y_h = list()
for point in poligon_point:
    f_y_h.append(3/2*point**2)

for i in range(M):
    my_X_sqrt += (n * (f_y_h[i] - poligon_h[i])**2) / f_y_h[i]

print(my_X_sqrt)

if my_X_sqrt > table_X_sqrt:
    print(my_X_sqrt.__str__() + " > " + table_X_sqrt.__str__() + "\nСледовательно: ")
    print("Выборка не соответствует теоретическому закону распределения по критерию Присона")
else:
    print(my_X_sqrt.__str__() + " < " + table_X_sqrt.__str__() + "\nСледовательно: ")
    print("Выборка соответствует теоретическому закону распределения по критерию Присона")
plt.show()