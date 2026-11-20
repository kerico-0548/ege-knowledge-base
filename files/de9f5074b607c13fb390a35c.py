# -*- coding: utf-8 -*-
# №19_3 (Уровень: Средний)
# Python: рекурсия any/all, игра на увеличение

from functools import lru_cache
@lru_cache(None)
def f(a,b,m):
    if a+b>=65: return m%2==0
    if m==0: return 0
    h = [f(a+1,b,m-1), f(a*3,b,m-1), f(a,b+1,m-1), f(a,b*3,m-1)]
    return any(h)
otvet = [s for s in range(1,59) if f(6,s,2)]
print(min(otvet))
