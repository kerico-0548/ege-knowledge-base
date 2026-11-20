# -*- coding: utf-8 -*-
# №23_3 Открытый вариант 2024 (Уровень: Лёгкий)
# Python: рекурсия по участкам и запрещённые точки

from functools import lru_cache
@lru_cache(None)
def f(x, y):
    if x > y: return 0
    if x == y: return 1
    return f(x+1, y) + f(x+2, y) + f(x*2, y)
print(f(4, 11) * f(11, 13) * f(13, 15))
