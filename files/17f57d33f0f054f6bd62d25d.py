# -*- coding: utf-8 -*-
# №16109 Резервный день 19.06.25 (Уровень: Повышенный)
# Python: две функции и предварительное заполнение

from functools import lru_cache
@lru_cache(None)
def g(n):
    if n <= 9: return 3*n
    return g(n-4)+2
def f(n): return g(n-1)+g(n-3)
for n in range(1,43000): g(n)
print(f(42999))
