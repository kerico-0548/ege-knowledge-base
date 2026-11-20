# -*- coding: utf-8 -*-
# №23_2 Демоверсия 2025 (Уровень: Лёгкий)
# Python: рекурсия по участкам и запрещённые точки

from functools import lru_cache
@lru_cache(None)
def f(x, y):
    if x < y: return 0
    if x == y: return 1
    return f(x-2, y) + f(x//2, y)
print(f(38, 16) * f(16, 2))
