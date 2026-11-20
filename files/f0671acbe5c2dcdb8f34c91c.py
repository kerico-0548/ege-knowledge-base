# -*- coding: utf-8 -*-
# №23_6 ЕГКР 2023 (Уровень: Средний)
# Python: рекурсия по участкам и запрещённые точки

from functools import lru_cache
@lru_cache(None)
def f(x, y):
    if x > y or x in (16,): return 0
    if x == y: return 1
    return f(x+1, y) + f(x+3, y) + f(x*x, y)
print(f(3, 20) * f(20, 26))
