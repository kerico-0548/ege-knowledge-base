# -*- coding: utf-8 -*-
# №15202 (Уровень: Лёгкий)
# Python: делимость и флаг

otvet = []
for a in range(1,100):
    flag = 0
    for x in range(0,1000):
        if (((x%a!=0) and (x%24==0)) <= ((x%16!=0) or (x%24!=0)))==False:
            flag = 1
            break
    if flag==0: otvet.append(a)
print(max(otvet))
