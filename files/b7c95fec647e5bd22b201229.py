# -*- coding: utf-8 -*-
# №8_11 Досрочная волна 2024 (Уровень: Средний)
# Python: product и номер слова

from itertools import product
k = 0
otvet = []
for x in product("АПРСУ",repeat=5):
    k += 1
    s = "".join(x)
    if s.count('У')<=1 and 'АА' not in s: otvet.append(k)
print(min(otvet))
