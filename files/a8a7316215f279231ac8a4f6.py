# -*- coding: utf-8 -*-
# №19_5 (Уровень: Повышенный)Авторская
# Python: рекурсия any/all, игра на уменьшение

from functools import lru_cache
@lru_cache(None)
def f(a,b,m):
    if a+b<=42: return m%2==0
    if m==0: return 0
    h = [f((a+2)//3,b,m-1), f(a,(b+2)//3,m-1)]
    if a>=4: h.append(f(a-4,b,m-1))
    if b>=4: h.append(f(a,b-4,m-1))
    return any(h) if (m-1)%2==0 else all(h)
otvet = [s for s in range(19,3403) if f(25,s,2)]
print(max(otvet))
