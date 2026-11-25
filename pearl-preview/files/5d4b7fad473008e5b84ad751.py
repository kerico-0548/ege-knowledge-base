# -*- coding: utf-8 -*-
# №21101 Демоверсия 2022 (Уровень: Очень лёгкий)
# Python: рекурсия any/all 

from functools import lru_cache
@lru_cache(None)
def f(s,m):
    if s>=29: return m%2==0
    if m==0: return 0
    h = [f(s+1,m-1), f(s*2,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
otvet = [s for s in range(1,29) if not f(s,2) and f(s,4)]
print(min(otvet))
