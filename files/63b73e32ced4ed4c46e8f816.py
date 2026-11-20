# -*- coding: utf-8 -*-
# №23101 (Уровень: Очень лёгкий)
# Python: рекурсия по участкам

from functools import lru_cache
@lru_cache(None)
def f(x, y):
    if x > y: return 0
    if x == y: return 1
    return f(x+1, y) + f(x*4, y)
print(f(3, 20))
