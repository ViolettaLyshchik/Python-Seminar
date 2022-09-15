# 29. Найти НОК двух чисел

from math import lcm

a = 10
b = 3

def get_lcm(a, b):
    return lcm(a, b)

print(get_lcm(a, b))