# -*- coding: utf-8 -*-
# 20_2) Для игры, описанной в задании 19, найдите два наименьших значения S, при которых у Пети есть выигрышная стратегия, причём одновременно выполняются два условия:
# Python: рекурсия any/all, игра на увеличение

from functools import lru_cache
@lru_cache(None)
def f(s,m):
    if s>=435: return m%2==0
    if m==0: return 0
    h = [f(s+5,m-1), f(s*3,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
otvet = [s for s in range(1,435) if not f(s,1) and f(s,3)]
print(*otvet[:2])
