# -*- coding: utf-8 -*-
# Примеры из ваших исходников. Импорт файла ничего не запускает.
# Каждый пример изолирован в функции primer_XX. Конкретные числа и пути принадлежат исходной задаче.
# Перед применением к новой задаче прочитайте предупреждения в PDF и сверьте условие.

# Источник: ЕГЭ_Инфа_ШПОРА_2026.docx, фрагмент 256
def primer_01():
    from itertools import product, permutations, combinations

    count = 0
    for x in product('ВИШНЯ', repeat=6):
        s = ''.join(x)

        if s.count('В') <= 1 and s[0] != 'Ш' and s[-1] != 'И' and s[-1] != 'Я':
            count += 1

    print(count)

# Источник: ЕГЭ_Инфа_ШПОРА_2026.docx, фрагмент 267
def primer_02():
    from itertools import product, permutations, combinations

    count = 0
    for x in permutations('012345', 5):
        s = ''.join(x)

        if s[0] != '0':
            s = s.replace('3', '1').replace('5', '1')
            s = s.replace('0', '2').replace('4', '2')

            if '212' not in s:
                count += 1

    print(count)

# Источник: ЕГЭ_Инфа_ШПОРА_2026.docx, фрагмент 276
def primer_03():
    from itertools import product, permutations, combinations

    count = 0
    for x in product('ЕКМОПРТЬЮ', repeat = 5):
        s = ''.join(x)

        count += 1
        if (count % 2 != 0) and (s[0] != 'Ь') and (s.count('К') == 2):
            print(count)

    print(count)

# Источник: Stepik: 03 - Комбинаторика (подсчёт слов), фрагмент 5162771
def primer_04():
    from itertools import product, permutations, combinations

    count = 0
    for x in permutations('012345', 5):
        s = ''.join(x)

        if s[0] != '0':
            s = s.replace('3', '1').replace('5', '1')
            s = s.replace('0', '2').replace('4', '2')

            if '212' not in s:
                count += 1


    print(count)

# Источник: Stepik: 05 - Порядок слов, фрагмент 5162779
def primer_05():
    from itertools import product, permutations, combinations

    count = 0
    for x in product('ЕКМОПРТЬЮ', repeat = 5):
        s = ''.join(x)

        count += 1
        if (count % 2 != 0) and (s[0] != 'Ь') and (s.count('К') == 2):
            print(count)


    print(count)

if __name__ == "__main__":
    print("Доступные примеры: primer_01, primer_02, primer_03, primer_04, primer_05")
    print("Вызовите нужную функцию осознанно; данные исходной задачи могут потребовать отдельного файла.")
