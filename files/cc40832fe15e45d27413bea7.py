# -*- coding: utf-8 -*-
# №16101 (Уровень: Очень лёгкий)
# Python: рекурсия, кэш и предварительное заполнение

from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
@lru_cache(None)
def f(n):
    if n <= 2: return n
    return f(n-1)+3*f(n-2)
for n in range(1, 100): f(n)
print(f(6))
