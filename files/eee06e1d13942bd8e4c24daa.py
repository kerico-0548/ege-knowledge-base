# -*- coding: utf-8 -*-
# №16_2 Апробация 2023 (Уровень: Лёгкий)
# Python: рекурсия, кэш и предварительное заполнение

from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
@lru_cache(None)
def f(n):
    if n >= 2025: return n
    return n+3+f(n+3)
print(f(2018)-f(2022))
