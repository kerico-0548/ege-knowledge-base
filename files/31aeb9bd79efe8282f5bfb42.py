# -*- coding: utf-8 -*-
# №8207 Основная волна 2023 (Уровень: Средний)
# Python: product и номер слова

from itertools import product
k = 0
otvet = []
for x in product("ЕКМОПРТЬЮ",repeat=5):
    k += 1
    s = "".join(x)
    if k%2==1 and s[0]!='Ь' and s.count('К')==2: otvet.append(k)
print(max(otvet))
