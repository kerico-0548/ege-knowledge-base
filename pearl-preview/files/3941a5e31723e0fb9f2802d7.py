# -*- coding: utf-8 -*-
# №8201 Демоверсия 2020 (Уровень: Очень лёгкий)
# Python: номер слова

from itertools import product
k = 0
for x in product("ИКНОТ", repeat=4):
    k += 1
    s = "".join(x)
    if s[0]=="О":
        print(k)
        break
