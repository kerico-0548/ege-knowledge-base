# -*- coding: utf-8 -*-
# №2_2 (Уровень: Лёгкий)
# Python + ручное сопоставление таблицы

for x in range(2):
    for y in range(2):
        for z in range(2):
            f1 = int(bool(((not x) and y and z) or ((not x) and (not y) and z) or ((not x) and (not y) and (not z))))
            if f1 == 1:
                print(x, y, z, f1)
