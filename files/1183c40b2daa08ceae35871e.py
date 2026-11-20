# -*- coding: utf-8 -*-
# №5102 Демоверсия 2021 (Уровень: Лёгкий)
# Python: bin, преобразование строки, список otvet

otvet = []
for n in range(1, 1000):
    s = bin(n)[2:]
    for _ in range(2):
        s += str(s.count('1')%2)
    r = int(s, 2)
    if r > 77: otvet.append(n)
print(min(otvet))
