# -*- coding: utf-8 -*-
# №2_8  (Уровень: Средний)
# Python + ручное сопоставление таблицы

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f1 = int(bool(((not x) and y and z and (not w)) or ((not x) and y and (not z) and (not w)) or (x and y and z and (not w))))
                if f1 == 1:
                    print(x, y, z, w, f1)
