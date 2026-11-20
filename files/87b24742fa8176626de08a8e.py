# -*- coding: utf-8 -*-
# №15501 (Уровень: Лёгкий)
# Python: отрезки и длина

d = 0
for a1 in range(12,54):
    for a2 in range(a1,54):
        flag = 0
        for t in range(0,541):
            x = t/10
            if (((a1<=x<=a2) <= (12<=x<=26)) or (30<=x<=53))==False:
                flag = 1
                break
        if flag==0: d = max(d,a2-a1)
print(d)
