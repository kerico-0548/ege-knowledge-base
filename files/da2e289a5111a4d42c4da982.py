# -*- coding: utf-8 -*-
# №17008 (Уровень: Сложный)
# Python: сумма цифр подходящих элементов, старый формат №17

ans = []
for x in range(-100000, 100001):
    s = str(abs(x))
    k = sum(int(c) for c in s)
    if k>13 and k%2==0 and s.endswith('3'):
        ans.append(k)
print(len(ans), sum(ans))
