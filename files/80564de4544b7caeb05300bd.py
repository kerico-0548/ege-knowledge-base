# -*- coding: utf-8 -*-
# №5_2 Основная волна 2024 (Уровень: Лёгкий)
# Python: bin и ветви алгоритма

otvet = []
for n in range(1,1000):
    s = bin(n)[2:]
    for _ in range(2):
        s += str(s.count('1')%2)
    r = int(s,2)
    if r>75: otvet.append(r)
print(min(otvet))
