# -*- coding: utf-8 -*-
# №16108 (Уровень: Повышенный)
# Python: несколько рекурсивных функций

from functools import lru_cache
@lru_cache(None)
def f(n):
    if n == 1: return 1
    return f(n-1) * g(n-1) + h(n-1)
@lru_cache(None)
def g(n):
    if n == 1: return 2
    return h(n) - g(n-1) + 3*n
@lru_cache(None)
def h(n):
    if n == 1: return 3
    return h(n-1) - n
print(f(5) * g(30) * h(50))
