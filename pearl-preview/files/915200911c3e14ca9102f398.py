# -*- coding: utf-8 -*-
# Демоверсия ФИПИ 2027 · №16
# Python / ручной: рекурсия и точное сокращение

import sys
sys.setrecursionlimit(10000)
def f(n):
    if n==1: return 1
    return n*f(n-1)
print((f(3038)+5*f(3037))//f(3036))
