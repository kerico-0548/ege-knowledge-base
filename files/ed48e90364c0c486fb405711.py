# -*- coding: utf-8 -*-
# №23201 Основная волна 2021 (Уровень: Очень лёгкий)
# Python: рекурсия и обязательные/запрещённые точки

from functools import lru_cache
@lru_cache(None)
def f(c,e):
    if c<e: return 0
    if c==e: return 1
    return f(c-2,e)+f(c-5,e)
print(f(23,2))
