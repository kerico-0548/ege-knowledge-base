# -*- coding: utf-8 -*-
# Открытый вариант ФИПИ 2026 · №13
# Ручной / Python: маска сети

from ipaddress import ip_network
net = ip_network("68.203.243.87/255.255.224.0",False)
ip = net[-2]
print(sum(map(int,str(ip).split("."))))
