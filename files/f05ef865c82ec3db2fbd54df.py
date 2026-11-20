# -*- coding: utf-8 -*-
# №2102 (Уровень: Лёгкий)
# Python + ручное сопоставление таблицы

for x in range(2):
    for y in range(2):
        for z in range(2):
            f1 = int(bool(z <= (x and (not y))))
            if f1 == 0:
                print(x, y, z, f1)
