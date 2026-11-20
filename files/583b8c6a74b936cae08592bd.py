# -*- coding: utf-8 -*-
# №14205 (Уровень: Средний)
# Python: подстановка неизвестной цифры

otvet = []
for x in "0123456789AB":
    for y in "0123456789AB":
        r = int(f"17{x}2{y}", 12) + int(f"{x}31{y}A6", 17)
        if r % 7 == 0: otvet.append(r)
print(min(otvet)//7)
