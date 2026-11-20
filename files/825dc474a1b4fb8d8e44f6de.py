# -*- coding: utf-8 -*-
# №5_4 Демоверсия 2025 (Уровень: Лёгкий-Средний)
# Python: bin и ветви алгоритма

otvet = []
for n in range(1,13):
    s = bin(n)[2:]
    s = '10'+s if n%2==0 else '1'+s+'01'
    r = int(s,2)
    if True: otvet.append(r)
print(max(otvet))
