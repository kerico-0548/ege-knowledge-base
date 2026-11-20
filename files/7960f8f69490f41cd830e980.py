# -*- coding: utf-8 -*-
# №15102 Демоверсия 2024 (Уровень: Лёгкий)
# Python: два цикла и выход из обоих

otvet = []
for a in range(201):
    flag = 0
    for x in range(61):
        for y in range(61):
            if ((x+2*y<a) or (y>x) or (x>60))==False:
                flag = 1
                break
        if flag==1: break
    if flag==0: otvet.append(a)
print(min(otvet))
