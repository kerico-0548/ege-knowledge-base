# -*- coding: utf-8 -*-
# №2208 (Уровень: Средний)
# Python + ручное сопоставление таблицы

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f1 = int(bool(((x or y) <= z) and (not (x == w))))
                if f1 == 1:
                    print(x, y, z, w, f1)
