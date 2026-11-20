# -*- coding: utf-8 -*-
# №14_4 Досрочная волна 2024 (Уровень: Лёгкий-Средний)
# Python: подстановка неизвестной цифры

for x in "QPONMLKJIHGFEDCBA9876543210":
    r = int(f"123{x}24", 27) + int(f"135{x}78", 27)
    if r % 26 == 0:
        print(r//26)
        break
