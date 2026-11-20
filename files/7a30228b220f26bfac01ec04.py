# -*- coding: utf-8 -*-
# Примеры из ваших исходников. Импорт файла ничего не запускает.
# Каждый пример изолирован в функции primer_XX. Конкретные числа и пути принадлежат исходной задаче.
# Перед применением к новой задаче прочитайте предупреждения в PDF и сверьте условие.

# Источник: 24.docx, фрагмент 5
def primer_01():
    f = open(r'c:/Users/Admin/Desktop/Задания24/24_1.txt')
    s = f.read()
    k=1
    kmax=0
    for i in range(0, len(s)-1):
        if s[i] != s[i+1]:
            k += 1
            kmax=max(k, kmax)
        else:
            k=1
    print(kmax)

# Источник: 24.docx, фрагмент 26
def primer_02():
    f = open(r'c:/Users/Admin/Desktop/Задания24/24_2.txt')
    s = f.read()
    k=1
    kmax=0
    for i in range(0, len(s)-1):
        if s[i] == 'P' and s[i + 1] == 'P':
            k = 1
        else:
            k += 1
            kmax=max(k, kmax)
    print(kmax)

# Источник: 24.docx, фрагмент 44
def primer_03():
    f = open(r'c:/Users/Admin/Desktop/Задания24/24_11.txt')
    s = f.read()
    k=0
    kmax=0
    s = s.replace('G', '*').replace('W', '*').replace('P', '*')
    for i in range(0, len(s)-1):
        if s[i] == '*':
            k = 0
        else:
            k += 1
            kmax = max(k, kmax)
    print(kmax)

# Источник: 24.docx, фрагмент 65
def primer_04():
    f = open(r'c:/Users/Admin/Desktop/Задания24/24_15.txt')
    s = f.read()
    k=1
    kmax=0
    s = s.replace('N', '*').replace('O', '*').replace('P', '*')
    for i in range(0, len(s)-1):
        if s[i] == '*' and s[i+1] == '*':
            k += 1
            kmax = max(k, kmax)
        else:
            k = 1
    print(kmax)

# Источник: 24.docx, фрагмент 86
def primer_05():
    f = open(r'c:/Users/Admin/Desktop/Задания24/24_20.txt')
    s = f.read()
    k=0
    kmax=0
    # print(s)
    for i in '0123456789ABCFED': s = s.replace(i, '*')
    for i in range (0,len(s)-1):
        if s[i]=='*':
            k += 1
            kmax = max(k,kmax)
        else:
            k = 0
    print(kmax)

# Источник: 24.docx, фрагмент 105
def primer_06():
    f = open(r'c:/Users/Admin/Desktop/Задания24/24_36.txt').readline()
    f = f.replace('A', '*').replace("B", '*').replace("C", '*')
    k = 0
    kmax = 0
    for i in range(0, len(f)):
        if f[i] == '*':
            k += 1
            kmax = max(kmax, k)
        else:
            k = 0
    print(kmax)

# Источник: 24.docx, фрагмент 123
def primer_07():
    f = open(r'c:/Users/Admin/Desktop/Задания24/24_16.txt')
    s = f.read()
    k=1
    kmax=0
    # print(s)
    cnt = 0
    maxi = 0
    for i in range (0,len(s)-1):
        if (s[i]=='d' and s[i+1]=='a') or (s[i]=='a' and s[i+1]=='d'):
            maxi = max(cnt+1,maxi)
            cnt = 0
        else:
            cnt += 1
    print(maxi)

# Источник: 24.docx, фрагмент 145
def primer_08():
    f = open(r'c:/Users/Admin/Desktop/Задания24/24_18.txt')
    s = f.read()
    k=1
    kmax=0
    s = s.replace('NPON', '*').replace('POON', '*')
    for i in range(0, len(s)-1):
        if s[i] == '*':
            k += 1
            kmax = max(k, kmax)
        else:
            k = 0
    print(kmax)

# Источник: 24.docx, фрагмент 163
def primer_09():
    f = open(r'c:/Users/Admin/Desktop/Задания24/24_21.txt')
    s = f.read()
    k=0
    kmax=0
    # print(s)
    s = s.replace('A', 'B').replace('C', 'B').replace('8', '9')
    for i in range (0,len(s)-1):
        if (s[i]=='B' and s[i+1] == '9') or (s[i]=='9' and s[i+1] == 'B'):
            k = 1
        else:
            k += 1
            kmax = max(k,kmax)
    print(kmax)

# Источник: 24.docx, фрагмент 182
def primer_10():
    f = open(r'c:/Users/Admin/Desktop/Задания24/24_31.txt').readline()
    k = 2
    kmax = 0
    for i in range(2, len(f)):
        if f[i-2] == 'X' and f[i-1] == 'Y' and f[i] == 'Z':
            k = 2
        else:
            k += 1
            kmax = max(k, kmax)
    print(kmax)

# Источник: 24.docx, фрагмент 199
def primer_11():
    f = open(r'c:/Users/Admin/Desktop/Задания24/24_27.txt')
    s = f.read()
    kmax = 0
    k = 1
    for i in range(len(s) - 1):
        if s[i:i+2] in 'KLMNK':
            k += 1
            kmax = max(kmax, k)
        else:
            k = 1
    print(kmax)

# Источник: 24.docx, фрагмент 213
def primer_12():
    f = open(r'c:/Users/Admin/Desktop/Задания24/24_28.txt').readline()
    f = f.replace('Q', 'R').replace('W', 'R').replace('2', '1').replace('4', '1')
    count_num = 0
    count_let = 0
    max_num = 0
    max_let = 0
    for i in range(len(f)):
        if f[i] == 'R' and f[i+1] == 'R':
            count_let += 1
            max_let = max(count_let, max_let)
        else:
            count_let = 1
        if f[i] == '1' and f[i+1] == '1':
            count_num += 1
            max_num = max(count_num, max_num)
        else:
            count_num = 1
    print(max_let, max_num)

# Источник: 24.docx, фрагмент 241
def primer_13():
    f = open(r'c:/Users/Admin/Desktop/Задания24/24_29.txt')
    s = f.read()
    kmax = 0
    k = 1
    for i in range(len(s) - 1):
        if s[i:i+2] in 'RSQR':
            k += 1
            kmax = max(kmax, k)
        else:
            k = 1
    print(kmax)

# Источник: 24.docx, фрагмент 259
def primer_14():
    f = open(r'c:/Users/Admin/Desktop/Задания24/24_3.txt')
    s = f.read()
    k=1
    kmax=0
    s = s.replace('O', 'A').replace('D', 'C').replace('F', 'C')
    s = s.replace('AC', '*')
    for i in range(0, len(s)-1):
        if s[i] == '*':
            k += 1
            kmax = max(k, kmax)
        else:
            k = 0
    print(kmax)

# Источник: 24.docx, фрагмент 280
def primer_15():
    f = open(r'c:/Users/Admin/Desktop/Задания24/24_6.txt')
    s = f.read()
    k=1
    kmax=0
    s = s.replace('AC', '*').replace('AB', '*')
    for i in range(0, len(s)-1):
        if s[i] == '*':
            k += 1
            kmax = max(k, kmax)
        else:
            k = 0
    print(kmax)

# Источник: 24.docx, фрагмент 298
def primer_16():
    f = open(r'c:/Users/Admin/Desktop/Задания24/24_7.txt')
    s = f.read()
    k=1
    kmax=0
    s = s.replace('Q', '*').replace('R', '*').replace('S', '*')
    for i in range(0, len(s)-1):
        if s[i] == '*' and s[i+1] == '*':
            k = 1
        else:
            k += 1
            kmax = max(k, kmax)
    print(kmax)

# Источник: 24.docx, фрагмент 320
def primer_17():
    f = open(r'c:/Users/Admin/Desktop/Задания24/24_8.txt')
    s = f.read()
    k=1
    kmax=0
    s = s.replace('X', '*').replace('Z', '*').replace('Y', '*')
    for i in range(0, len(s)-1):
        if s[i] == '*' and s[i+1] == '*':
            k = 1
        else:
            k += 1
            kmax = max(k, kmax)
    print(kmax)

# Источник: 24.docx, фрагмент 339
def primer_18():
    f = open(r'c:/Users/Admin/Desktop/Задания24/24_9.txt')
    s = f.read()
    k=1
    kmax=0
    for i in 'BC':
        s = s.replace(i, 'A')
    for i in '789':
        s = s.replace(i, '6')
    for i in range(0, len(s)-1):
        if (s[i] == 'A' and s[i+1] == 'A') or (s[i] == '6' and s[i+1] == '6'):
            k = 1
        else:
            k += 1
            kmax = max(k, kmax)
    print(kmax)

# Источник: 24.docx, фрагмент 361
def primer_19():
    f = open(r'c:/Users/Admin/Desktop/Задания24/24_10.txt')
    s = f.read()
    k=1
    kmax=0
    s = s.replace('E', 'A').replace('B', 'C').replace('D', 'C')
    s = s.replace('AC', '*')
    for i in range(0, len(s)-1):
        if s[i] == '*':
            k += 1
            kmax = max(k, kmax)
        else:
            k = 0
    print(kmax)

# Источник: 24.docx, фрагмент 383
def primer_20():
    f = open(r'c:/Users/Admin/Desktop/Задания24/24_12.txt')
    s = f.read()
    k=1
    kmax=0
    s = s.replace('AB', '*').replace('AC', '*')
    for i in range(0, len(s)-1):
        if s[i] == '*':
            k += 1
            kmax = max(k, kmax)
        else:
            k = 0
    print(kmax)

# Источник: 24.docx, фрагмент 402
def primer_21():
    f = open(r'c:/Users/Admin/Desktop/Задания24/24_13.txt')
    s = f.read()
    k1=0
    kmax1=0
    k2=0
    kmax2=0
    s = s.replace('BA', '*').replace('DA', '!')
    print(s)
    for i in range(0, len(s)):
        if s[i] == '*':
            k1 += 1
            kmax1 = max(k1, kmax1)
        else:
            k1 = 0
        if s[i] == '!':
            k2 += 1
            kmax2 = max(k2, kmax2)
        else:
            k2 = 0
    print(kmax1, kmax2)

# Источник: 24.docx, фрагмент 431
def primer_22():
    f = open(r'c:/Users/Admin/Desktop/Задания24/24_14.txt')
    s = f.read()
    k=1
    kmax=0
    s = s.replace('CFE', '*').replace('FCE', '*')
    for i in range(0, len(s)-1):
        if s[i] == '*':
            k += 1
            kmax = max(k, kmax)
        else:
            k = 0
    print(kmax)

# Источник: 24.docx, фрагмент 467
def primer_23():
    f = open(r'c:/Users/Admin/Desktop/Задания24/24_31.txt').readline()
    k = 3
    kmax = 0
    for i in range(3, len(f)):
        if f[i-3] == 'X' and f[i-2] == 'Z' and f[i-1] == 'Z' and f[i] == 'Y':
            k = 3
        else:
            k += 1
            kmax = max(k, kmax)
    print(kmax)

# Источник: 24.docx, фрагмент 517
def primer_24():
    f = open(r'c:/Users/Admin/Desktop/Задания24/24_4.txt')
    file = f.read()
    t = []
    for i in range(len(file)):
        if file[i] == 'T':
            t.append(i)
    max_diff = 0
    for i in range(len(t) - 101):
        diff = t[i+101] - t[i] - 1
        if diff > max_diff:
            max_diff = diff
    print(max_diff)

# Источник: 24.docx, фрагмент 532
def primer_25():
    f = open(r'c:/Users/Admin/Desktop/Задания24/24_19.txt')
    file = f.read()
    t = []
    for i in range(len(file)):
        if file[i] == 'Y':
            t.append(i)
    max_diff = 0
    for i in range(len(t) - 151):
        diff = t[i+151] - t[i] - 1
        if diff > max_diff:
            max_diff = diff
    print(max_diff)

# Источник: 24.docx, фрагмент 549
def primer_26():
    f = open(r'c:/Users/Admin/Desktop/Задания24/24_22.txt')
    file = f.read()
    # A, B, C, D, E и F cd
    t = []
    for i in range(len(file)):
        if file[i] == 'C' and file[i+1] == 'D':
            t.append(i)
    max_diff = 0
    for i in range(len(t) - 161):
        diff = t[i+161] - t[i]
        if diff > max_diff:
            max_diff = diff
    print(max_diff)

if __name__ == "__main__":
    print("Доступные примеры: primer_01, primer_02, primer_03, primer_04, primer_05, primer_06, primer_07, primer_08, primer_09, primer_10, primer_11, primer_12, primer_13, primer_14, primer_15, primer_16, primer_17, primer_18, primer_19, primer_20, primer_21, primer_22, primer_23, primer_24, primer_25, primer_26")
    print("Вызовите нужную функцию осознанно; данные исходной задачи могут потребовать отдельного файла.")

# --- ПРОВЕРЕННЫЕ БАЗОВЫЕ БЛОКИ ---
# Базовые блоки тех же методов k/kmax, replace и списка позиций.
# Исправлены начальные значения и обработка последнего символа/краёв строки.
def raznye_sosedi(s):
    k = 1 if s else 0
    kmax = k
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            k += 1
        else:
            k = 1
        kmax = max(k, kmax)
    return kmax

def cepochka_iz_nabora(s, allowed):
    k = 0
    kmax = 0
    for i in range(len(s)):
        if s[i] in allowed:
            k += 1
            kmax = max(k, kmax)
        else:
            k = 0
    return kmax

def rovno_k_simvolov(s, symbol, k):
    # Для одного символа; к перекрывающимся подстрокам автоматически не применять.
    if k < 1:
        raise ValueError('В этом шаблоне k должно быть положительным')
    t = [-1]
    for i in range(len(s)):
        if s[i] == symbol:
            t.append(i)
    t.append(len(s))
    kmax = 0
    for i in range(len(t) - k - 1):
        kmax = max(kmax, t[i + k + 1] - t[i] - 1)
    return kmax

def ne_bolee_k_simvolov(s, symbol, k):
    if k < 0:
        raise ValueError('k должно быть неотрицательным')
    if s.count(symbol) <= k:
        return len(s)
    if k == 0:
        return max((len(x) for x in s.split(symbol)), default=0)
    return rovno_k_simvolov(s, symbol, k)
