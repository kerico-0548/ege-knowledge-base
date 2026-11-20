# -*- coding: utf-8 -*-
# 21_4) Для игры, описанной в задании 19, найдите количество значений S, при котором одновременно выполняются два условия:
# Python: рекурсия any/all, игра на уменьшение

from functools import lru_cache
@lru_cache(None)
def f(s,m):
    if s<=12: return m%2==0
    if m==0: return 0
    h = [f(s//3,m-1), f(s-12,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
otvet = [s for s in range(13,1053) if not f(s,2) and f(s,4)]
print(len(otvet))
