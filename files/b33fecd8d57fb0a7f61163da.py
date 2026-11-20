# -*- coding: utf-8 -*-
# №16_8Р Открытый вариант 2024 (Уровень: Средний)
# Python: рекурсия, кэш и предварительное заполнение

from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
@lru_cache(None)
def f(n):
    if n == 1: return 1
    return n*f(n-1)
for n in range(1, 9000): f(n)
print((f(2024)-f(2023))//f(2022))
