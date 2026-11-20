# -*- coding: utf-8 -*-
# №2203 Апробация 2023 (Уровень: Лёгкий)
# Python + ручное сопоставление таблицы

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f1 = int(bool((not (z or (w <= y))) or (x <= z)))
                if f1 == 0:
                    print(x, y, z, w, f1)
