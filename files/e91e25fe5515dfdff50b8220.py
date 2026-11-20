# -*- coding: utf-8 -*-
# Демоверсия ФИПИ 2027 · №15
# Python: флаг и доказанные границы

otvet = []
for a in range(1,1000):
    flag = 0
    for x in range(1,1000):
        if ((x%a==0) or ((70<=x<=90) <= (x%22!=0)))==False:
            flag = 1
            break
    if flag==0: otvet.append(a)
print(max(otvet))
