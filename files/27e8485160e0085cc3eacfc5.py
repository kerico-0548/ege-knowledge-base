# -*- coding: utf-8 -*-
# №16202 Основная волна 2023 (Уровень: Лёгкий)
# Python: рекурсия, кэш и предварительное заполнение

from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
@lru_cache(None)
def f(n):
    if n < 11: return n
    return n+f(n-1)
for n in range(1, 9000): f(n)
print(f(2024)-f(2021))
