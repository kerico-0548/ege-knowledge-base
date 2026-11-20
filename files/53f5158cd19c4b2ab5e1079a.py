# -*- coding: utf-8 -*-
# №17004 (Уровень: Средний)
# Python: список подходящих чисел, старый формат №17

ans = []
for x in range(10000, 22223):
    if (x%10==7 or x%100==25) and x%2!=0:
        ans.append(x)
print(len(ans), min(ans))
