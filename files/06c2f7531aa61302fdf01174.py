# -*- coding: utf-8 -*-
# №5111 Основная волна 2024 (Уровень: Средний)
# Python: bin, преобразование строки, список otvet

otvet = []
for n in range(1, 13):
    s = bin(n)[2:]
    s = '10'+s if n%2==0 else '1'+s+'01'
    r = int(s, 2)
    if True: otvet.append(r)
print(max(otvet))
