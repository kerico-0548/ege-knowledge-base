# -*- coding: utf-8 -*-
# №5_6 Пересдача 2024 (Уровень: Средний)
# Python: bin и ветви алгоритма

otvet = []
for n in range(28,1000):
    s = bin(n)[2:]
    s = '10'+(s+'0')[2:] if s.count('1')%2==0 else '11'+(s+'1')[2:]
    r = int(s,2)
    if True: otvet.append(r)
print(min(otvet))
