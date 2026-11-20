# -*- coding: utf-8 -*-
# №13_9 (Уровень: Средний) Авторская​​
# Python / ручной: общий префикс двух адресов

from ipaddress import *
otvet = []
for p in range(33):
    net = ip_network('220.170.36.80/'+str(p), strict=False)
    if ip_address('220.170.36.75') in net:
        otvet.append(p)
print(max(otvet))
