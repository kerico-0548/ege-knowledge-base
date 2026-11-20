# -*- coding: utf-8 -*-
# №2_1 (Уровень: Очень лёгкий)
# Python + ручное сопоставление таблицы

for x in range(2):
    for y in range(2):
        for z in range(2):
            f1 = int(bool(((y or z) <= x) or (x == z)))
            if f1 == 0:
                print(x, y, z, f1)
