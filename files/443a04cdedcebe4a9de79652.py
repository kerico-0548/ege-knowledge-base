# -*- coding: utf-8 -*-
# №16_3 Пробник ИМЦ СПб (Уровень: Лёгкий)
# Python: рекурсия, кэш и предварительное заполнение

from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
@lru_cache(None)
def f(n):
    if n == 1: return 1
    return f(n-1)*(2*n-3)
for n in range(1, 9000): f(n)
print(f(516)//f(513))
