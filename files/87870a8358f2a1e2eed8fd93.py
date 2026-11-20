# -*- coding: utf-8 -*-
# 21_1) Для игры, описанной в задании 19, найдите значение S, при котором одновременно выполняются два условия:
# Python: рекурсия any/all, игра на увеличение

from functools import lru_cache
@lru_cache(None)
def f(s,m):
    if s>=67: return m%2==0
    if m==0: return 0
    h = [f(s+1,m-1), f(s+3,m-1), f(s*2,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
otvet = [s for s in range(1,67) if not f(s,2) and f(s,4)]
print(min(otvet))
