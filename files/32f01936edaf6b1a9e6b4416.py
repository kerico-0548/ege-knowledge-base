# -*- coding: utf-8 -*-
# №16104 (Уровень: Лёгкий)
# Python: рекурсия, кэш и предварительное заполнение

from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
@lru_cache(None)
def f(n):
    if n < 3: return 1
    if n%2 == 0: return f(n-2)-f(n-1)
    return 2*f(n-1)-f(n-2)
for n in range(1, 100): f(n)
print(f(18))
