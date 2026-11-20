# -*- coding: utf-8 -*-
# №17007 (Уровень: Повышенный)
# Python: два списка по двум отрезкам, старый формат №17

a = []
b = []
for x in range(-10510, 13568):
    if (x<0 and str(abs(x)).endswith('123')) or (x>0 and x%4==0 and x%7==0):
        a.append(x)
for x in range(17560, 46551):
    if x%4==0 and x%7==0:
        b.append(x)
print(len(a)+len(b), max(a)+max(b))
