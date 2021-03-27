import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plot

# Заданные параметры
n = 5.1
s = 17.3 # начальное расстояние от лодки до катера
fi = 3 * math.pi / 4

# Функция, описывающая движения катера береговой охраны
def f(r, tetha):
    dr = r/math.sqrt(n * n - 1)
    return dr

# Начальные условия для 1 случая:
r0 = s / (n + 1)
tetha = np.arange(0,2 * math.pi, 0.01)

# Начальные для 2 случая:
#r0 = s/(n-1)
#tetha = np.arange(-math.pi,math.pi, 0.01)

r = odeint(f, r0, tetha)

# Функция, описывающая движение лодки браконьеров
def f2(t):
    xt = math.tan(fi) * t
    return xt

t = np.arange(0,10,1)

r1 = np.sqrt(t * t + f2(t) * f2(t))

tetha1 = np.arctan(f2(t) / t)

# Построение графиков функций
plot.polar(tetha, r, 'b') # движение катера охраников
plot.polar(tetha1, r1, 'r') # движение лодки браконьеров

# Нахождение точки пересечения катера и лодки
tmp = 0
for i in range(len(tetha)):
    if round(tetha[i],2) == round(fi + math.pi, 2): # для 1 случая
   # if round(tetha[i],2) == round(fi - math.pi, 2): # для 2 случая
        tmp = i

print("Точка пересечения в полярных координатах: tetha = ", tetha[tmp], ", r = ", r[tmp][0])
print("Точка пересечения в декартовых координатах: x = ", r[tmp][0] * math.cos(fi), ", y = ", r[tmp][0] * math.sin(fi))