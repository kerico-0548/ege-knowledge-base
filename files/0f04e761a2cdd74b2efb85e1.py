# -*- coding: utf-8 -*-
# №2_9 Основная волна 2023 - пересдача (Уровень: Средний)
# Python + ручное сопоставление таблицы

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f1 = int(bool((x <= (z == w)) or (not (y <= w))))
                if f1 == 0:
                    print(x, y, z, w, f1)
