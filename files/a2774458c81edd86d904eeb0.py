# -*- coding: utf-8 -*-
# Демоверсия ФИПИ 2027 · №17
# Python: список и соседние пары

from pathlib import Path
f = Path(__file__).resolve().parents[2]/"Источники"/"ФИПИ демоверсия 2027"/"Доп_Файлы"/"demo_17.txt"
a = [int(x) for x in open(f)]
m = min(a)
ans = []
for i in range(len(a)-1):
    if a[i]%33==m or a[i+1]%33==m:
        ans.append(a[i]+a[i+1])
print(len(ans),max(ans))
