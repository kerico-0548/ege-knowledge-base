# -*- coding: utf-8 -*-
# №23_8 (Уровень: Средний)Авторская
# Python: рекурсия по участкам и запрещённые точки

from functools import lru_cache
@lru_cache(None)
def f(x, y):
    if x < y or x in (22,): return 0
    if x == y: return 1
    return f(x-2, y) + f(x-5, y) + f(x//3, y)
print(f(108, 41) * f(41, 12))
