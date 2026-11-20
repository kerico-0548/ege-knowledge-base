# -*- coding: utf-8 -*-
# №16106 (Уровень: Средний)
# Python: рекурсия с кешем

from functools import lru_cache
@lru_cache(None)
def f(n):
    if n == 1: return 1
    if n == 2: return 2
    if n % 2 == 0: return (n + f(n-2)) // 5
    return (2*n + f(n-1) + f(n-2)) // 4
print(f(50))
