# -*- coding: utf-8 -*-
# Примеры из ваших исходников. Импорт файла ничего не запускает.
# Каждый пример изолирован в функции primer_XX. Конкретные числа и пути принадлежат исходной задаче.
# Перед применением к новой задаче прочитайте предупреждения в PDF и сверьте условие.

# Источник: ЕГЭ_Инфа_ШПОРА_2026.docx, фрагмент 428
def primer_01():
    for A in range(1, 100):
        flag = False
        for x in range(1, 1000):
            if ((x % A != 0) <= ((x % 14 == 0) <= (x % 4 != 0))) == False:
                flag = True
                break
        if flag == False:
            print(A)

# Источник: ЕГЭ_Инфа_ШПОРА_2026.docx, фрагмент 441
def primer_02():
    for A in range(1, 1000):
        flag = False
        for x in range(1, 300):
            for y in range(1, 300):
                if ((4*x < y) or (x >= 10) or (x * y < A)) == False:
                    flag = True
                    break
            if flag == True:
                break
        if flag == False:
            print(A)

# Источник: ЕГЭ_Инфа_ШПОРА_2026.docx, фрагмент 453
def primer_03():
    for A in range(1, 1000):
        flag = False
        for x in range(1, 1000):
            if (((x & 42 != 0) and (x&34 == 0)) <= (x & A != 0)) == 0:
                flag = True
                break
        if flag == False:
            print(A)

# Источник: ЕГЭ_Инфа_ШПОРА_2026.docx, фрагмент 470
def primer_04():
    p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30}
    q = {1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31}
    a = set()

    for x in range(1, 1000):
        if (((x not in p) <= (x in a)) or ((x not in a) <= (x not in q))) == False:
            a.add(x)

    print(len(a))    # выводим длину получившегося множества

# Источник: ЕГЭ_Инфа_ШПОРА_2026.docx, фрагмент 485
def primer_05():
    ln = 0
    for a1 in range(6, 430+1):
        for a2 in range(a1 + 1, 430+1):
            flag = False
            for x in range(0, 430+1):
                P = (250 <= x <= 430)
                Q = (60 <= x <= 320)
                A = (a1 <= x <= a2)
                if ((P <= Q) <= (not A)) == False:
                    flag = True
                    break
            if flag == False:
                ln = max(ln, a2 - a1)

    print(ln/10)    # делим на 10, т.к. в начале умножили на 10

# Источник: Stepik: 08 - Объединение нескольких прототипов, фрагмент 5157334
def primer_06():
    for A in range(1, 1000):
        flag = False
        for x in range(1, 1000):
            if(((x % 3 == 0) <= (x % 5 != 0)) or (x + A >= 70)) == False:
                flag = True
                break
        if flag == False:
            print(A)

if __name__ == "__main__":
    print("Доступные примеры: primer_01, primer_02, primer_03, primer_04, primer_05, primer_06")
    print("Вызовите нужную функцию осознанно; данные исходной задачи могут потребовать отдельного файла.")
