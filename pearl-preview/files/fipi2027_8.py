from itertools import product
k = 0
for x in product("АЕКНТЦ",repeat=5):
    k += 1
    s = "".join(x)
    if k%2==0 and s[0] not in "АЕК" and s.count("Т")>=1:
        print(k)
        break
