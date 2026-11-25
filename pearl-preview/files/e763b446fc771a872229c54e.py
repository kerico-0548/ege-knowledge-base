# -*- coding: utf-8 -*-
# №17002 Основная волна 2021 (Уровень: Лёгкий)
# Python: список подходящих чисел, старый формат №17

ans = []
for x in range(22015, 56457):
    if (x%5==0 or x%13==0) and all(x%d!=0 for d in (7,11,15)):
        ans.append(x)
print(len(ans), min(ans))
