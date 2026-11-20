# -*- coding: utf-8 -*-
# №20201 Демоверсия 2021 (Уровень: Лёгкий)
# Python: рекурсия any/all 

from functools import lru_cache
@lru_cache(None)
def f(a,b,m):
    if a+b>=77: return m%2==0
    if m==0: return 0
    h = [f(a+1,b,m-1), f(a*2,b,m-1), f(a,b+1,m-1), f(a,b*2,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
otvet = [s for s in range(1,70) if not f(7,s,1) and f(7,s,3)]
print(*otvet[:2])
