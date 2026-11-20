# -*- coding: utf-8 -*-
# №5110 (Уровень: Повышенный)
# Python: шестнадцатеричная запись

for n in range(1,250401):
    s = hex(n)[2:]
    flag = any(c in 'abcdef' for c in s)
    if flag: s = '5'+s+'7'
    else: s = '7'+s+'5'
    r = int(s,16)
    if r>250400:
        print(n)
        break
