# -*- coding: utf-8 -*-
# №23106 Демоверсия 2024 (Уровень: Средний)
# Python: рекурсия по участкам

from functools import lru_cache
@lru_cache(None)
def f(x, y):
    if x > y or x in (11,): return 0
    if x == y: return 1
    return f(x+1, y) + f(x*2, y) + f(x*x, y)
print(f(2, 20))
