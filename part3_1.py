import matplotlib.pyplot as plt
import numpy as np
from creature_Y import get_Y

n = 200
M = 8
Y = get_Y(n)
fig, ax = plt.subplots(1, 1, figsize=(16, 9))

m = n // M
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
    plt.bar((A[yi] + B[yi]) / 2,
              m / (n * (B[yi] - A[yi])),
              width=B[yi] - A[yi])
    x_point_2.append((A[yi] + B[yi]) / 2)
    polygon_h_2.append(m / (n * (B[yi] - A[yi])))
plt.plot(x_point_2, polygon_h_2, color='black')

x_theoretical = np.linspace(-1, 1, 3000)
f_y = list()
for xi in x_theoretical:
    f_y.append(3/2*xi**2)
plt.plot(x_theoretical, f_y, color='blue', label='Теоретическая плотность распределения')
plt.plot(x_point_2, polygon_h_2, color='r', label='Эмпирическая плотность распределения')


my_X_sqrt = 0
table_X_sqrt = 20.1 # a = 0,01 k = 8
pi_theoretical = list()
pi = [m / n] * M
for i in range(0, M):
    F_Ai = 0.5 * ((A[i])**3+1)
    F_Bi = 0.5 * ((B[i])**3+1)
    pi_theoretical.append(F_Bi - F_Ai)

for i in range(M):
    my_X_sqrt += n * (pi_theoretical[i] - pi[i]) ** 2 / pi_theoretical[i]


print(my_X_sqrt)

if my_X_sqrt > table_X_sqrt:
    print(my_X_sqrt.__str__() + " > " + table_X_sqrt.__str__() + "\nСледовательно: ")
    print("Выборка не соответствует теоретическому закону распределения по критерию Присона")
else:
    print(my_X_sqrt.__str__() + " < " + table_X_sqrt.__str__() + "\nСледовательно: ")
    print("Выборка соответствует теоретическому закону распределения по критерию Присона")
plt.show()