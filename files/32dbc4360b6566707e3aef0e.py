# -*- coding: utf-8 -*-
# №2204 (Уровень: Лёгкий)
# Python + ручное сопоставление таблицы

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f1 = int(bool((x or y) and (w <= z) and (not y)))
                if f1 == 1:
                    print(x, y, z, w, f1)
