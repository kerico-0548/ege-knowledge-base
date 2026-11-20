# -*- coding: utf-8 -*-
# №19201 Демоверсия 2021 (Уровень: Лёгкий) (Демо2021) 19.1)
# Python: рекурсия any/all 

from functools import lru_cache
@lru_cache(None)
def f(a,b,m):
    if a+b>=77: return m%2==0
    if m==0: return 0
    h = [f(a+1,b,m-1), f(a*2,b,m-1), f(a,b+1,m-1), f(a,b*2,m-1)]
    return any(h)
otvet = [s for s in range(1,70) if f(7,s,2)]
print(min(otvet))
