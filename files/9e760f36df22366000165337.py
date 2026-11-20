# -*- coding: utf-8 -*-
# №16107 (Уровень: Повышенный)
# Python: несколько рекурсивных функций

from functools import lru_cache
@lru_cache(None)
def f(n):
    if n == 1: return 2
    return f(n-1) * 2 * g(n-1)
@lru_cache(None)
def g(n):
    if n == 1: return 1
    return g(n-1) + 2*n
print(f(7) * g(12))
