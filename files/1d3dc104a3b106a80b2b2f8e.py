# -*- coding: utf-8 -*-
# №16205 (Уровень: Средний)
# Python: рекурсия, кэш и предварительное заполнение

from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
@lru_cache(None)
def f(n):
    if n == 1: return 3
    if n%2 == 0: return f(n-1)+5
    return f(n-1)+7
for n in range(1, 9000): f(n)
print(f(8765))
