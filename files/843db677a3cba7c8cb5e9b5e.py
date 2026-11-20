# -*- coding: utf-8 -*-
# №16_7Р  ЕГКР 2024 (Уровень: Средний)
# Python: рекурсия, кэш и предварительное заполнение

from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
@lru_cache(None)
def f(n):
    if n <= 3: return 2025
    return 3*(n-1)*f(n-2)
for n in range(1, 9000): f(n)
print(f(2027)//f(2023))
