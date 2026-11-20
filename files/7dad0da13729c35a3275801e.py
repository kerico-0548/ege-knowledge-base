# -*- coding: utf-8 -*-
# Примеры из ваших исходников. Импорт файла ничего не запускает.
# Каждый пример изолирован в функции primer_XX. Конкретные числа и пути принадлежат исходной задаче.
# Перед применением к новой задаче прочитайте предупреждения в PDF и сверьте условие.

# Источник: 25.docx, фрагмент 1
def primer_01():
    from fnmatch import fnmatch, fnmatchcase
    count = 0
    for n in range(1917, 10**10+1, 1917):
        if fnmatch(str(n), '3?12?14*5'):
            print(n, n//1917)
    print(count)

# Источник: 25.docx, фрагмент 10
def primer_02():
    from fnmatch import fnmatch, fnmatchcase
    count = 0
    for n in range(2024, 10**10+1, 2024):
        if fnmatch(str(n), '1?2157*4'):
            print(n, n//2024)

# Источник: 25.docx, фрагмент 18
def primer_03():
    from fnmatch import fnmatch, fnmatchcase
    count = 0
    for n in range(122, 10**10+1, 2421):
        if fnmatch(str(n), '78?2*435'):
            if n % 2421 == 122:
                print(n, n//2421)

# Источник: 25.docx, фрагмент 27
def primer_04():
    from fnmatch import fnmatch, fnmatchcase
    count = 0
    for n in range(2111, 10**11+1, 2111):
        if fnmatch(str(n), '2?*1?474*5'):
            count += 1
    print(count)

# Источник: 25.docx, фрагмент 36
def primer_05():
    count = 0
    for n in range(12357, 10**8+1, 12357):
        s = str(n)
        if (s[0] == "1" and s[2] == "5" and s[-1] == "6") and s[1] in '13579':
            print(s, int(s)//12357)

# Источник: 25.docx, фрагмент 57
def primer_06():
    x = 205602
    y = 217743
    for i in range(x, y+1):
        c = set()
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                c.add(j)
                c.add(i // j)
        if len(c) == 3:
            print(*sorted(c))

# Источник: 25.docx, фрагмент 69
def primer_07():
    x = 1010500
    y = 1010700
    for i in range(x, y+1):
        c = set()
        for j in range(2, int(i ** 0.5)):
            if i % j == 0:
                c.add(j)
                c.add(i // j)
        if len(c) == 4:
            print(*sorted(c)[2:])

# Источник: 25.docx, фрагмент 81
def primer_08():
    x = 122222
    y = 122322
    for i in range(x, y+1):
        c = set()
        for j in range(1, int(i ** 0.5)+1):
            if i % j == 0:
                c.add(j)
                c.add(i // j)
        if len(c) == 2:
            print(*sorted(c)[1:])

# Источник: 25.docx, фрагмент 93
def primer_09():
    x = 10000
    y = 10019
    for i in range(x, y+1):
        c = set()
        for j in range(1, int(i ** 0.5)):
            if i % j == 0:
                c.add(j)
                c.add(i // j)
        if len(c) == 4:
            print(*sorted(c)[1:3])

# Источник: 25.docx, фрагмент 106
def primer_10():
    x = 174457
    y = 174505
    for i in range(x, y+1):
        c = set()
        for j in range(2, int(i ** 0.5)):
            if i % j == 0:
                c.add(j)
                c.add(i // j)
        if len(c) == 2:
            print(*sorted(c))

# Источник: 25.docx, фрагмент 120
def primer_11():
    x = 800_000
    y = 800_033
    for i in range(x, y+1):
        c = set()
        for j in range(2, int(i ** 0.5)):
            if i % j == 0:
                c.add(j)
                c.add(i // j)
        if len(c) > 1:
            m = max(c) + min(c)
            if m % 10 == 4:
                print(i, m)

# Источник: 25.docx, фрагмент 139
def primer_12():
    x = 700_000
    y = 700_033
    for i in range(x, y+1):
        c = set()
        for j in range(2, int(i ** 0.5)):
            if i % j == 0:
                c.add(j)
                c.add(i // j)
        if len(c) > 1:
            m = max(c) + min(c)
            if m % 10 == 8:
                print(i, m)

# Источник: 25.docx, фрагмент 156
def primer_13():
    x = 700_000
    y = 700_133
    for i in range(x, y+1):
        c = set()
        for j in range(2, int(i ** 0.5)):
            if i % j == 0:
                c.add(j)
                c.add(i // j)
        if len(c) > 1:
            m = sum(sorted(c)[-2:])
            if m % 10 == 4:
                print(i, m)

# Источник: 25.docx, фрагмент 174
def primer_14():
    x = 250_200
    y = 255_200
    for i in range(x, y+1):
        c = set()
        for j in range(2, int(i ** 0.5)):
            if i % j == 0:
                c.add(j)
                c.add(i // j)
        if len(c) > 1:
            m = sum(sorted(c)[:2])
            if m % 123 == 17:
                print(i, m)

# Источник: 25.docx, фрагмент 189
def primer_15():
    x = 130000
    y = 140000
    for i in range(x, y+1):
        c = set()
        for j in range(2, int(i ** 0.5)):
            if i % j == 0:
                c.add(j)
                c.add(i // j)
        # print(sum(c))
        if len(c) >= 2:
            if max(c) - min(c) <= 65002:
                print(i, max(c) - min(c))

# Источник: 25.docx, фрагмент 204
def primer_16():
    x = 700_000
    y = 700_033
    for i in range(x, y+1):
        c = set()
        for j in range(2, int(i ** 0.5)):
            if i % j == 0:
                c.add(j)
                c.add(i // j)
        k = 0
        kk = []
        for k7 in c:
            if k7 % 10 == 7 and k7 != i and k7 != 7:
                k += 1
                kk.append(k7)
        if k >= 1:
            print(i, min(kk))

# Источник: 25.docx, фрагмент 224
def primer_17():
    x = 800_000
    y = 800_033
    for i in range(x, y+1):
        c = set()
        for j in range(1, int(i ** 0.5)):
            if i % j == 0:
                c.add(j)
                c.add(i // j)
        k = 0
        kk = []
        for k9 in c:
            if k9 % 10 == 9 and k9 != i and k9 != 9:
                k += 1
                kk.append(k9)
        if k >= 1:
            print(i, min(kk))

# Источник: 25.docx, фрагмент 245
def primer_18():
    x = 200_000
    y = 600_000
    for i in range(x, y+1):
        c = set()
        for j in range(2, int(i ** 0.5)+1):
            if i % j == 0 and i % 2 == 0:
                c.add(j)
                c.add(i // j)
        k = 0
        for ch in sorted(c):
            if ch % 2 == 0:
                k += 1
        if len(c) == k and k != 0:
            print(i, max(c))

# Источник: 25.docx, фрагмент 262
def primer_19():
    x = 100000
    y = 400000
    for i in range(x, y+1):
        c = set()
        for j in range(2, int(i ** 0.5)):
            if i % j == 0 and j % 2 == 0:
                c.add(j)
            if i % j == 0 and (i // j) % 2 == 0:
                c.add(i // j)
        # print(sum(c))
        if sum(c) == 5986:
            print(*sorted(c))

# Источник: 25.docx, фрагмент 277
def primer_20():
    x = 500000
    y = 510000
    for i in range(x, y+1):
        c = set()
        for j in range(1, int(i ** 0.5)):
            if i % j == 0 and j % 2 == 0:
                c.add(j)
            if i % j == 0 and (i // j) % 2 == 0:
                c.add(i // j)
        if sum(c) % 10 == 8:
            print(i, sum(c))

# Источник: 25.docx, фрагмент 290
def primer_21():
    from fnmatch import fnmatch, fnmatchcase
    count = 0
    for n in range(0, 10**7+1):
        if fnmatch(str(n), '1??5*1'):
            c = set()
            for d in range(1, int(n**0.5) + 1):
                if n % d == 0:
                    c.add(d)
                    c.add(n//d)
            if len(c) == 3:
                print(*sorted(c)[1:-1])

if __name__ == "__main__":
    print("Доступные примеры: primer_01, primer_02, primer_03, primer_04, primer_05, primer_06, primer_07, primer_08, primer_09, primer_10, primer_11, primer_12, primer_13, primer_14, primer_15, primer_16, primer_17, primer_18, primer_19, primer_20, primer_21")
    print("Вызовите нужную функцию осознанно; данные исходной задачи могут потребовать отдельного файла.")


# --- ПРОВЕРЕННЫЕ БАЗОВЫЕ БЛОКИ ---
# Парные делители через set: тот же способ, что в 25.docx.
# Квадратный корень включён; исключения 1 и n управляются отдельно.
def deliteli(n, bez_edinicy=False, bez_chisla=False):
    c = set()
    for j in range(1, int(n ** 0.5) + 1):
        if n % j == 0:
            c.add(j)
            c.add(n // j)
    if bez_edinicy:
        c.discard(1)
    if bez_chisla:
        c.discard(n)
    return sorted(c)

def maska(limit, d, mask, ostatok=0):
    from fnmatch import fnmatch
    answer = []
    start = ostatok if ostatok else d
    for n in range(start, limit + 1, d):
        if n > 0 and fnmatch(str(n), mask):
            answer.append((n, n // d))
    return answer
