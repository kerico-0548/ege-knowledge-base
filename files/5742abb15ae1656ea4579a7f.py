# -*- coding: utf-8 -*-
# №8205 (Уровень: Средний)
# Python: product и номер слова

from itertools import product
k = 0
otvet = []
for x in product("АЙЛМ",repeat=5):
    k += 1
    s = "".join(x)
    if s.count('М')<=1 and 'ЛЛ' not in s: otvet.append(k)
print(max(otvet))
