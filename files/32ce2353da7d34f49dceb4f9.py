# -*- coding: utf-8 -*-
# Примеры из ваших исходников. Импорт файла ничего не запускает.
# Каждый пример изолирован в функции primer_XX. Конкретные числа и пути принадлежат исходной задаче.
# Перед применением к новой задаче прочитайте предупреждения в PDF и сверьте условие.

# Источник: ЕГЭ_Инфа_ШПОРА_2026.docx, фрагмент 606
def primer_01():
    # одна куча, +1 *2 s>=50

    def f(s, m): # s - кол-во камней m - кол-во ходов
        if s >= 25: return m % 2 == 0
        if m == 0:  return 0 # игра не закончилась
        h = [f(s+2, m-1), f(s*2, m-1)]
        # выигрышная стратегия должна существоввать в одном из ходов заверршающего игрока
        # и во все= ходах другого игрока.
        return any(h) if (m-1) % 2 == 0 else all(h)

    # m = 1 (П1);m = 2 (В1 ГАРАНТИРОВАННО) ;m = 3 (П2) ;m = 4 (В12)
    print('19)',[s for s in range(1, 25) if f(s, 2)]) # список из значений s, только при В1
    print('20)', [s for s in range(1, 25) if not f(s, 1) and f(s, 3)])
    print('21)', [s for s in range(1, 25) if not f(s, 2) and f(s, 4)])

# Источник: ЕГЭ_Инфа_ШПОРА_2026.docx, фрагмент 634
def primer_02():
    def f(a, b, m):
        if a + b >= 45: return m % 2 == 0
        if m == 0: return 0
        h = [f(a+1, b, m - 1), f(a*3, b, m - 1), f(a, b+1, m-1), f(a, b*3, m-1)]
        return any(h) if (m - 1) % 2 == 0 else all(h)

    print('19)',[s for s in range(1, 41) if f(4, s, 2)]) # список из значений s, только при В1
    print('20)', [s for s in range(1, 41) if not f(4, s, 1) and f(4, s, 3)])
    print('21)', [s for s in range(1, 41) if not f(4, s, 2) and f(4, s, 4)])

# Источник: ЕГЭ_Инфа_ШПОРА_2026.docx, фрагмент 646
def primer_03():
    def f(a, b, m):
        if a + b <= 26: return m % 2 == 0
        if m == 0: return 0
        h = [f(a-4, b, m - 1), f(a//2+a%2, b, m - 1), f(a, b-4, m-1), f(a, b//2+b%2, m-1)]
        return any(h) if (m - 1) % 2 == 0 else all(h) # all - замени на any в 19

    print('19)',[s for s in range(16, 100) if f(15, s, 2)]) # список из значений s, только при В1
    print('20)', [s for s in range(16, 100) if not f(15, s, 1) and f(15, s, 3)])
    print('21)', [s for s in range(16, 100) if not f(15, s, 2) and f(15, s, 4)])

if __name__ == "__main__":
    print("Доступные примеры: primer_01, primer_02, primer_03")
    print("Вызовите нужную функцию осознанно; данные исходной задачи могут потребовать отдельного файла.")
