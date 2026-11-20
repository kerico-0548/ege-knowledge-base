# -*- coding: utf-8 -*-
# №23_11 ФИПИ (Уровень: Сложный)
# Python: перебор количества команд

otvet = set()
for a in range(69):
    b = 68-a
    otvet.add(1 + 3*a - 2*b)
print(len(otvet))
