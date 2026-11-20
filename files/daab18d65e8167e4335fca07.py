# -*- coding: utf-8 -*-
# №5_8 (Уровень: Средний)
# Python: последовательные арифметические шаги

otvet = []
for n in range(2,31):
    r = n
    for d in (2,3,5):
        if r%d==0: r //= d
        else: r -= 1
    if r==1: otvet.append(n)
print(len(otvet))
