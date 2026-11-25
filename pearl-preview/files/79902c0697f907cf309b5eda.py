# -*- coding: utf-8 -*-
# №17003 (Уровень: Лёгкий)
# Python: список подходящих чисел, старый формат №17

ans = []
for x in range(12014, 49636):
    if x%13==7 and x%5!=0 and x%12!=0 and x%10==3:
        ans.append(x)
print(len(ans), min(ans))
