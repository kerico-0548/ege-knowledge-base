# -*- coding: utf-8 -*-
# №16_9Р Основная волна 2023 - 2 день (Уровень: Средний)
# Python: рекурсия, кэш и предварительное заполнение

from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
@lru_cache(None)
def f(n):
    if n < 7: return 7
    return n+1+f(n-2)
for n in range(1, 9000): f(n)
print(f(2024)-f(2020))
