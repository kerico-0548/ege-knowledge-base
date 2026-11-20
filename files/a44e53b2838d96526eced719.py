# -*- coding: utf-8 -*-
# №23103 (Уровень: Лёгкий)
# Python: рекурсия по участкам

from functools import lru_cache
@lru_cache(None)
def f(x, y):
    if x > y or x in (12,): return 0
    if x == y: return 1
    return f(x+3, y) + f(x*2, y)
print(f(2, 40))
