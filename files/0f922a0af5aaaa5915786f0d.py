# -*- coding: utf-8 -*-
# №23_5 ЕГКР 2024 (Уровень: Средний)
# Python: рекурсия по участкам и запрещённые точки

from functools import lru_cache
@lru_cache(None)
def f(x, y):
    if x > y or x in (16,): return 0
    if x == y: return 1
    return f(x+1, y) + f(x+2, y) + f(x*3, y)
print(f(2, 9) * f(9, 18))
