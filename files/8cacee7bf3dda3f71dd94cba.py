# -*- coding: utf-8 -*-
# №2_4 Пересдача 2024 (Уровень: Средний)
# Python + ручное сопоставление таблицы

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f1 = int(bool((z <= (not (y <= x))) or w))
                if f1 == 0:
                    print(x, y, z, w, f1)
