# -*- coding: utf-8 -*-
# №14204 (Уровень: Лёгкий)
# Python: подстановка неизвестной цифры

otvet = []
for x in "0123456":
    r = int(f"216{x}341", 7) + int(f"1B{x}14C", 15)
    if r % 3 == 0: otvet.append(r)
print(sum(otvet))
