# -*- coding: utf-8 -*-
# Открытый вариант ФИПИ 2026 · №17
# Python: список и соседние пары

from pathlib import Path
f = Path(__file__).resolve().parents[2]/"Источники"/"ФИПИ открытый вариант 2026"/"Доп. файлы"/"1_17.txt"
a = [int(x) for x in open(f)]
m = min(x for x in a if x>0 and x%123==0)
ans = []
for i in range(len(a)-1):
    if a[i]+a[i+1]<m: ans.append(a[i]+a[i+1])
print(len(ans),abs(max(ans)))
