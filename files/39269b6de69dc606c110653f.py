# -*- coding: utf-8 -*-
# №19_2 ЕГКР 2024 (Уровень: Средний)
# Python: рекурсия any/all, игра на увеличение

from functools import lru_cache
@lru_cache(None)
def f(s,m):
    if s>=435: return m%2==0
    if m==0: return 0
    h = [f(s+5,m-1), f(s*3,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
otvet = [s for s in range(1,435) if f(s,2)]
print(min(otvet))
