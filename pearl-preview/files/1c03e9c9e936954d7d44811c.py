# -*- coding: utf-8 -*-
# №16103 Демоверсия 2022 (Уровень: Лёгкий)
# Python: рекурсия, кэш и предварительное заполнение

from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
@lru_cache(None)
def f(n):
    if n == 1: return 1
    if n%2 == 0: return n+f(n-1)
    return 2*f(n-2)
for n in range(1, 100): f(n)
print(f(26))
