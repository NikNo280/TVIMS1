import matplotlib.pyplot as plt
import numpy as np
from creature_Y import get_Y
np.random.seed(666)


n = 50
Y = get_Y(n)
fig, ax = plt.subplots(1, 1, figsize=(16, 9))
Fn = []
F = []
my_squared_deviation = 0

for i in range(1, n+1):
    Fn.append((i - 0.5) / n)
    F.append(((Y[i-1])**3+1)/2)
    my_squared_deviation += ((Fn[i - 1] - F[i - 1]) ** 2)
my_squared_deviation += 1 / (12 * n)

table_my_squared_deviation = 0.461# a = 0.05
if my_squared_deviation > table_my_squared_deviation:
    print(my_squared_deviation.__str__() + " > " + table_my_squared_deviation.__str__() + "\nСледовательно: ")
    print("Выборка не соответствует теоретическому закону распределения по критерию Мизеса")
else:
    print(my_squared_deviation.__str__() + " < " + table_my_squared_deviation.__str__() + "\nСледовательно: ")
    print("Выборка соответствует теоретическому закону распределения по критерию Мизеса")