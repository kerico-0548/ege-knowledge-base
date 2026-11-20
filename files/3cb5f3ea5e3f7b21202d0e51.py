# -*- coding: utf-8 -*-
# №14206 Демоверсия 2026 (Уровень: Повышенный)
# Python: подстановка неизвестной цифры

for x in "SRQPONMLKJIHGFEDCBA9876543210":
    r = int(f"923{x}874", 29) + int(f"524{x}6152", 29)
    if r % 28 == 0:
        print(r//28)
        break
