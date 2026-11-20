# -*- coding: utf-8 -*-
# №5101 Демоверсия 2021 (Уровень: Очень лёгкий)
# Python: bin, преобразование строки, список otvet

otvet = []
for n in range(1, 1000):
    s = bin(n)[2:]
    for _ in range(2):
        s += str(int(s,2)%2)
    r = int(s, 2)
    if r > 98: otvet.append(n)
print(min(otvet))
