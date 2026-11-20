# -*- coding: utf-8 -*-
# №16203 (Уровень: Лёгкий)
# Python: рекурсия, кэш и предварительное заполнение

from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
@lru_cache(None)
def f(n):
    if n <= 3: return 1
    return (n+3)*f(n-2)
for n in range(1, 9000): f(n)
print(f(2028)//f(2024))
