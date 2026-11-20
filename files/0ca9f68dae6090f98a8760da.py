# -*- coding: utf-8 -*-
# №8_9 Пересдача 2024 (Уровень: Средний)
# Python: product и номер слова

from itertools import product
k = 0
otvet = []
for x in product("АЙЛМ",repeat=5):
    k += 1
    s = "".join(x)
    if 'М' not in s and 'Л' not in s and 'ЙЙ' not in s: otvet.append(k)
print(max(otvet))
