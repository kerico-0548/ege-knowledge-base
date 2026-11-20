# -*- coding: utf-8 -*-
# №8204 Досрочная волна 2023 (Уровень: Лёгкий)
# Python: product и номер слова

from itertools import product
k = 0
otvet = []
for x in product("АКЛМНЯ",repeat=5):
    k += 1
    s = "".join(x)
    if s.startswith('КМ'): otvet.append(k)
print(min(otvet))
