# -*- coding: utf-8 -*-
# №23105 Досрочная волна 2023 (Уровень: Средний)
# Python: рекурсия и обязательные/запрещённые точки

from functools import lru_cache
@lru_cache(None)
def f(c,e):
    if c>e or c==13: return 0
    if c==e: return 1
    return f(c+1,e)+f(c+2,e)+f(c*3,e)
print(f(3,8)*f(8,18))
