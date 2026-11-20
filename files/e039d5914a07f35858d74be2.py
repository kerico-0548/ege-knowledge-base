# -*- coding: utf-8 -*-
# №15_12 (Уровень: Средний) 
# Python: отрезки, перебор границ и поиск контрпримера

p1, p2 = (133, 175)
q1, q2 = (140, 199)
granicy = sorted({p1, p2, q1, q2})
otvet = []
for a1 in granicy:
    for a2 in granicy:
        if a1 > a2:
            continue
        flag = False
        for t in range(2*min(granicy)-1, 2*max(granicy)+2):
            x = t / 2
            p = p1 <= x <= p2
            q = q1 <= x <= q2
            a = a1 <= x <= a2
            if not ((not p) <= ((q and (not a)) <= p)):
                flag = True
                break
        if not flag:
            otvet.append(a2-a1)
print(min(otvet))
