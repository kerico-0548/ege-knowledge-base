# -*- coding: utf-8 -*-
# №23102 Демоверсия 2021 (Уровень: Лёгкий)
# Python: рекурсия и обязательные/запрещённые точки

from functools import lru_cache
@lru_cache(None)
def f(c,e):
    if c>e: return 0
    if c==e: return 1
    return f(c+1,e)+f(c*2,e)
print(f(1,10)*f(10,20))
