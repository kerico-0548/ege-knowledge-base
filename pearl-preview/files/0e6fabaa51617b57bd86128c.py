# -*- coding: utf-8 -*-
# №20202 Основная волна 2022 (Уровень: Средний)
# Python: рекурсия any/all 

from functools import lru_cache
@lru_cache(None)
def f(a,b,m):
    if a+b>=259: return m%2==0
    if m==0: return 0
    h = [f(a+1,b,m-1), f(a*2,b,m-1), f(a,b+1,m-1), f(a,b*2,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
otvet = [s for s in range(1,242) if not f(17,s,1) and f(17,s,3)]
print(*otvet[:2])
