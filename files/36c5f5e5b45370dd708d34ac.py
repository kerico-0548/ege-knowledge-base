# -*- coding: utf-8 -*-
# №23_10 СтатГрад (Уровень: Сложный)
# Новый подтип: рекурсия с признаком предыдущей команды

from functools import lru_cache
@lru_cache(None)
def f(x, a):
    if x == 15: return 1
    if x > 16 or x < 2: return 0
    k = f(x*2, False) + f(x*3, False)
    if not a:
        k += f(x-1, True)
    return k
print(f(3, False))
