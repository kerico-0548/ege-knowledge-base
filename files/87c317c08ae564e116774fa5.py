# -*- coding: utf-8 -*-
# №15601 (Уровень: Лёгкий)
# Python: делимость и неравенство

otvet = []
for a in range(1,100):
    flag = 0
    for x in range(1,100):
        if (((x%2==0) <= (x%3!=0)) or (x+a>=80))==False:
            flag = 1
            break
    if flag==0: otvet.append(a)
print(min(otvet))
