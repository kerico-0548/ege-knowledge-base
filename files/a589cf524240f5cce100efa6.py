# -*- coding: utf-8 -*-
# Примеры из ваших исходников. Импорт файла ничего не запускает.
# Каждый пример изолирован в функции primer_XX. Конкретные числа и пути принадлежат исходной задаче.
# Перед применением к новой задаче прочитайте предупреждения в PDF и сверьте условие.

# Источник: ЕГЭ_Инфа_ШПОРА_2026.docx, фрагмент 497
def primer_01():
    def f(n):
        if n <= 3:
            return n
        elif n > 2:
            return f(n-2) + 2 * f(n-4)
    print(f(27))    # вызов функции

# Источник: ЕГЭ_Инфа_ШПОРА_2026.docx, фрагмент 501
def primer_02():
    import sys
    sys.setrecursionlimit(10000)

    def f(n):
        if n <= 3:
            return n
        elif n > 2:
            return f(n-2) + 2 * f(n-4)
    print(f(27))

# Источник: ЕГЭ_Инфа_ШПОРА_2026.docx, фрагмент 505
def primer_03():
    from functools import lru_cache

    @lru_cache(None)
    def f(n):
        if n <= 3:
            return n
        elif n > 2:
            return f(n-2) + 2 * f(n-4)
        
    for n in range(1, 3000):
        f(n)
        
    print(f(27))

# Источник: ЕГЭ_Инфа_ШПОРА_2026.docx, фрагмент 510
def primer_04():
    import sys
    sys.setrecursionlimit(100000)

    def f(n):
        if n < 17:
            return 6
        if n >= 17:
            return (n+5) * f(n-9)

    # print( (f(234561) / 436 + f(234552) / 218) / f(234534) ) # Ошибка
    print( (f(234561) // 436 + f(234552) // 218) // f(234534) )

# Источник: ЕГЭ_Инфа_ШПОРА_2026.docx, фрагмент 527
def primer_05():
    import sys
    sys.setrecursionlimit(100000)

    def f(n):
        return g(n-1) + g(n-3)

    def g(n):
        if n <= 9:
            return 3*n
        if n > 9:
            return g(n-4)+2

    print(f(42999))

if __name__ == "__main__":
    print("Доступные примеры: primer_01, primer_02, primer_03, primer_04, primer_05")
    print("Вызовите нужную функцию осознанно; данные исходной задачи могут потребовать отдельного файла.")
