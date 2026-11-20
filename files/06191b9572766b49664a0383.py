# -*- coding: utf-8 -*-
# №17001 Демоверсия 2021 (Уровень: Очень лёгкий)
# Python: список подходящих чисел, старый формат №17

ans = []
for x in range(1016, 7938):
    if x%3==0 and all(x%d!=0 for d in (7,17,19,27)):
        ans.append(x)
print(len(ans), max(ans))
