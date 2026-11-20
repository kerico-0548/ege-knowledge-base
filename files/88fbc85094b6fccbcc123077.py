# -*- coding: utf-8 -*-
# №19203 (Уровень: Повышенный)
# Python: рекурсия any/all с уменьшением

from functools import lru_cache
@lru_cache(None)
def f(a,b,m):
    if a+b<=26: return m%2==0
    if m==0: return 0
    h = [f(a-4,b,m-1), f((a+1)//2,b,m-1), f(a,b-4,m-1), f(a,(b+1)//2,m-1)]
    return any(h)
otvet = [s for s in range(16,417) if f(15,s,2)]
print(max(otvet))
