# -*- coding: utf-8 -*-
# Открытый вариант ФИПИ 2026 · №23
# Python: рекурсия с условной командой

from functools import lru_cache
@lru_cache(None)
def f(c,e):
    if c>e or c==14: return 0
    if c==e: return 1
    return f(c+1,e)+f(c*2,e)+f(c*3,e)
print(f(2,39))
