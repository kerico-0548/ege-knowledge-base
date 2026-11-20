# -*- coding: utf-8 -*-
# №16105 (Уровень: Лёгкий)
# Python: рекурсия, кэш и предварительное заполнение

from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
@lru_cache(None)
def f(n):
    if n < 5: return 1+2*n
    if n%3 == 0: return 2*(n+1)*f(n-2)
    return 2*n+1+f(n-1)+2*f(n-2)
for n in range(1, 100): f(n)
print(f(15))
