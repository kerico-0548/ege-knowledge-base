# -*- coding: utf-8 -*-
# №15201 Демоверсия 2021 (Уровень: Лёгкий)
# Python: делимость и флаг

otvet = []
for a in range(1,100):
    flag = 0
    for x in range(1,1000):
        if ((x%a!=0) <= ((x%6==0) <= (x%9!=0)))==False:
            flag = 1
            break
    if flag==0: otvet.append(a)
print(max(otvet))
