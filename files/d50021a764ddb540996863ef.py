# -*- coding: utf-8 -*-
# Примеры из ваших исходников. Импорт файла ничего не запускает.
# Каждый пример изолирован в функции primer_XX. Конкретные числа и пути принадлежат исходной задаче.
# Перед применением к новой задаче прочитайте предупреждения в PDF и сверьте условие.

# Источник: ЕГЭ_Инфа_ШПОРА_2026.docx, фрагмент 542
def primer_01():
    f = open('27629.txt')
    s = [int(x) for x in f]

    k42 = -10**10
    maxi = -10**10
    count = 0

    for j in range(1, len(s)):
        if abs(s[j]) % 100 == 43:
            if (1000 <= abs(s[j]) <= 9999):
                k42 = max(k42, s[j])

    for i in range(1, len(s)):
        if ((1000 <= abs(s[i-1]) <= 9999) + (1000 <= abs(s[i]) <= 9999)) >= 1:
            if (s[i-1] + s[i])**2 < k42**2:
                count += 1
                maxi = max(maxi, (s[i-1] + s[i])**2)
                
    print(count, maxi)

# Источник: Stepik: 03 - Устаревшая. Отрезки, фрагмент 5652047
def primer_02():
    mini = 10**10
    count = 0
    for i in range(16015, 48989+1):
        if (i % 7 == 0 or i % 11 == 0) and (i % 9 != 0 and i % 12 != 0 and i % 13 != 0):
            count += 1
            mini = min(mini, i)
    print(count, mini)

# Источник: Stepik: 04 - Обработка числовой последовательности, фрагмент 5163013
def primer_03():
    f = open('task17.txt')
    s = [int(x) for x in f]

    count = 0
    maks_summa = ok_13 = -1000000

    for k in range(0, len(s)):    # Нахождение числа, оканчивающегося на 13
        if s[k] % 100 == 13:
            ok_13 = max(ok_13, s[k])

    for i in range(0, len(s) - 2):
        dlina = 0
        for j in range(0, 3):    # Нахождение двух трёхзначных чисел
            if 100 <= s[i + j] <= 999:
                dlina += 1

        summa = s[i] + s[i+1] + s[i+2]    # Сумма всех чисел

        if (dlina == 2) and (summa <= ok_13):    # Основное условие
            count += 1
            maks_summa = max(maks_summa)

    print(count, maks_summa)


if __name__ == "__main__":
    print("Доступные примеры: primer_01, primer_02, primer_03")
    print("Вызовите нужную функцию осознанно; данные исходной задачи могут потребовать отдельного файла.")

# --- ПРОВЕРЕННЫЕ БАЗОВЫЕ БЛОКИ ---
# Список подходящих сумм: по «ещё/17», третий снимок.
# Вместо привязки к 17.txt список передаётся в функцию.
# Пустой ответ обозначен None, чтобы не вызывать max([]).
def pari_s_kratnym_3(a):
    ans = []
    for i in range(len(a)-1):
        if a[i] % 3 == 0 or a[i+1] % 3 == 0:
            ans.append(a[i] + a[i+1])
    return len(ans), max(ans) if ans else None
