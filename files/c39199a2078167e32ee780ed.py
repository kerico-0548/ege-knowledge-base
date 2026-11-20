# -*- coding: utf-8 -*-
# №16102 Демоверсия 2024 (Уровень: Очень лёгкий)
# Python: рекурсия, кэш и предварительное заполнение

from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
@lru_cache(None)
def f(n):
    if n > 2024: return n
    return n*f(n+1)
print(f(2022)//f(2024))
