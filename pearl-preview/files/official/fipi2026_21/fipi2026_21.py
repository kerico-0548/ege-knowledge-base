# -*- coding: utf-8 -*-
# Открытый вариант ФИПИ 2026 · №21
# Python: any/all и исключение ранней победы

from functools import lru_cache
@lru_cache(None)
def f(a,b,m):
    if a+b>=154: return m%2==0
    if m==0: return 0
    h = [f(a+4,b,m-1),f(a*3,b,m-1),f(a,b+4,m-1),f(a,b*3,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
print(min(s for s in range(1,143) if not f(11,s,2) and f(11,s,4)))
