# -*- coding: utf-8 -*-
# №16_1 ФИПИ (Уровень: Лёгкий)
# Python: рекурсия, кэш и предварительное заполнение

from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
@lru_cache(None)
def f(n):
    if n < 3: return 1
    if n%2 == 0: return f(n-1)+n-1
    return f(n-2)+2*n-2
for n in range(1, 9000): f(n)
print(f(33))
