# -*- coding: utf-8 -*-
# №8202 (Уровень: Очень лёгкий) 
# Python: номер слова

from itertools import product
k = 0
for x in product("ВГЛО", repeat=5):
    k += 1
    if k==333:
        print("".join(x))
        break
