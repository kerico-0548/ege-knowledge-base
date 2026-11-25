# -*- coding: utf-8 -*-
# №19202 Основная волна 2022 (Уровень: Средний)
# Python: рекурсия any/all 

from functools import lru_cache
@lru_cache(None)
def f(a,b,m):
    if a+b>=259: return m%2==0
    if m==0: return 0
    h = [f(a+1,b,m-1), f(a*2,b,m-1), f(a,b+1,m-1), f(a,b*2,m-1)]
    return any(h)
otvet = [s for s in range(1,242) if f(17,s,2)]
print(min(otvet))
