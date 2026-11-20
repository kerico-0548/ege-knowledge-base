# -*- coding: utf-8 -*-
# Примеры из ваших исходников. Импорт файла ничего не запускает.
# Каждый пример изолирован в функции primer_XX. Конкретные числа и пути принадлежат исходной задаче.
# Перед применением к новой задаче прочитайте предупреждения в PDF и сверьте условие.

# Источник: ЕГЭ_Инфа_ШПОРА_2026.docx, фрагмент 695
def primer_01():
    def f(start, end):
        if start > end or start == 10:
            return 0
        elif start == end:
            return 1
        else:
            return f(start+1, end) + f(start * 2, end)

    print(f(2,10) * f(10, 20))

# Источник: ЕГЭ_Инфа_ШПОРА_2026.docx, фрагмент 705
def primer_02():
    def f(start, end):
        if start > end:
            return f(start - 1, end) + f(start // 2, end)
        elif start == end:
            return 1
        elif start < end:
            return 0

    print(f(40, 15) * f(15, 2))

if __name__ == "__main__":
    print("Доступные примеры: primer_01, primer_02")
    print("Вызовите нужную функцию осознанно; данные исходной задачи могут потребовать отдельного файла.")


# --- ПРОВЕРЕННЫЕ БАЗОВЫЕ БЛОКИ ---
# По двум снимкам из «ещё»: условные команды, исходная рекурсивная схема.
# В перестановке последние две цифры вместо индексов только для трёхзначного числа.
# Тестовый пример первого снимка: f_perestav(100, 150).
def f_perestav(c, e):
    p = str(c)
    if c > e: return 0
    if c == e: return 1
    res = f_perestav(c+1, e)
    if len(p) >= 2 and p[-2] < p[-1]:
        res += f_perestav(int(p[:-2]+p[-1]+p[-2]), e)
    return res

# Второй снимок: +2 или заменить первую слева 1 на 3; от 10 до 44.
def f_zamena(x, y):
    if x > y: return 0
    if x == y: return 1
    res = f_zamena(x+2, y)
    a = str(x)
    if a.count('1') > 0:
        a = a.replace('1', '3', 1)
        res += f_zamena(int(a), y)
    return res
