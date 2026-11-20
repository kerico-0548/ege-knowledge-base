# -*- coding: utf-8 -*-
# №20203 (Уровень: Повышенный)
# Python: рекурсия any/all с уменьшением

from functools import lru_cache
@lru_cache(None)
def f(a,b,m):
    if a+b<=26: return m%2==0
    if m==0: return 0
    h = [f(a-4,b,m-1), f((a+1)//2,b,m-1), f(a,b-4,m-1), f(a,(b+1)//2,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
otvet = [s for s in range(16,417) if not f(15,s,1) and f(15,s,3)]
print(min(otvet), max(otvet))
