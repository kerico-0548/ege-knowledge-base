# -*- coding: utf-8 -*-
# №15301 (Уровень: Лёгкий)
# Python: поразрядная конъюнкция

otvet = []
for a in range(128):
    flag = 0
    for x in range(128):
        if (((x&39)==0) or (((x&11)==0) <= ((x&a)!=0)))==False:
            flag = 1
            break
    if flag==0: otvet.append(a)
print(min(otvet))
