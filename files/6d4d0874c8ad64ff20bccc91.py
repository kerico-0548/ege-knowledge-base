# -*- coding: utf-8 -*-
# №19_4 Пробник ИМЦ СПб 2024 (Уровень: Повышенный)
# Python: рекурсия any/all, игра на уменьшение

from functools import lru_cache
@lru_cache(None)
def f(s,m):
    if s<=12: return m%2==0
    if m==0: return 0
    h = [f(s//3,m-1), f(s-12,m-1)]
    return any(h)
otvet = [s for s in range(13,1053) if f(s,2)]
print(max(otvet))
