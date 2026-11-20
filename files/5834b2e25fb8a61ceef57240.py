# -*- coding: utf-8 -*-
# Примеры из ваших исходников. Импорт файла ничего не запускает.
# Каждый пример изолирован в функции primer_XX. Конкретные числа и пути принадлежат исходной задаче.
# Перед применением к новой задаче прочитайте предупреждения в PDF и сверьте условие.

# Источник: ЕГЭ Задание 27\27 Новое\1 - Простая Кластеризация\Демо2025.docx, фрагмент 0
def primer_01():
    f = open('demo27')
    f.readline()
    cl1, cl2 = [], []
    for i in f:
        x, y = map(float, i.replace(',', '.').split())
        if -2 <= x <= 1 and 0 <= y <= 3:
            cl1.append((x, y))
        if 1 <= x <= 4.5 and 3 <= y <= 7:
            cl2.append((x, y))

    def centr(cluster):
        x_cent, y_cent, mini = 0, 0, 10**100
        for i in range(len(cluster)):
            res = 0
            for j in range(len(cluster)):
                x1, y1= cluster[i]
                x2, y2 = cluster[j]
                res += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            if res < mini:
                mini = res
                x_cent, y_cent = x1, y1
            return x_cent, y_cent

    x1, y1 = centr(cl1)
    x2, y2 = centr(cl2)

    print((x1 + x2) / 2 * 10000)
    print((y1 + y2) / 2 * 10000)
    f = open('demo27')
    f.readline()
    cl1, cl2, cl3 = [], [], []
    for i in f:
        x, y = map(float, i.replace(',', '.').split())
        if 0 <= x <= 2.5 and 0 <= y <= 3:
            cl1.append((x, y))
        if 2 <= x <= 4.5 and 6 <= y <= 11:
            cl2.append((x, y))
        if 5 <= x <= 8 and 4 <= y <= 7:
            cl3.append((x, y))

    def centr(cluster):
        x_cent, y_cent, mini = 0, 0, 10**100
        for i in range(len(cluster)):
            res = 0
            for j in range(len(cluster)):
                x1, y1 = cluster[i]
                x2, y2 = cluster[j]
                res += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            if res < mini:
                mini = res
                x_cent, y_cent = x1, y1
            return x_cent, y_cent

    x1, y1 = centr(cl1)
    x2, y2 = centr(cl2)
    x3, y3 = centr(cl3)

    print((x1 + x2 + x3) / 3 * 10000)
    print((y1 + y2 + y3) / 3 * 10000)

# Источник: ЕГЭ Задание 27\27 Новое\2 - Сложная Кластеризация\ЕГЭ Задание№27 ПЭ.docx, фрагмент 1
def primer_02():
    def centr(cluster):
        x_cent, y_cent, mini = 0, 0, 10**100
        for i in range(len(cluster)):
            res = 0
            for j in range(len(cluster)):
                x1, y1= cluster[i]
                x2, y2 = cluster[j]
                res += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            if res < mini:
                mini = res
                x_cent, y_cent = x1, y1
            return x_cent, y_cent

    x1, y1 = centr(cl1)
    x2, y2 = centr(cl2)

    print((x1 + x2) / 2 * 10000)
    print((y1 + y2) / 2 * 10000)

# Источник: ЕГЭ Задание 27\27 Новое\2 - Сложная Кластеризация\ЕГЭ Задание№27 ПЭ.docx, фрагмент 11
def primer_03():
    from math import dist  # Импортируем функцию dist для вычисления евклидова расстояния

    # 📌 Чтение данных из файла
    with open(
            r'D:\Репетиторство\ЕГЭ по ИНФ\Презентации\ЕГЭ Задание 27\27 Новое\2 - Сложная Кластеризация\27A_18623.txt') as f:
        f.readline()  # Пропускаем первую строку (заголовок)

        # Читаем координаты точек и добавляем их в список data
        data = [(float(x), float(y)) for x, y in (line.replace(',', '.').split() for line in f)]

    clusters = []  # Список кластеров
    eps = 1  # Пороговое расстояние (эпсилон) для объединения точек в один кластер


    # 📌 Функция для нахождения центра кластера (точка с минимальной суммой расстояний)
    def centr(cluster):
        r = []  # Список для хранения сумм расстояний и соответствующих точек

        for i in cluster:
            total_dist = sum(dist(i, j) for j in cluster)  # Считаем сумму расстояний от i до всех остальных
            r.append((total_dist, i))  # Добавляем кортеж (сумма расстояний, точка)

        return min(r)[1]  # Возвращаем точку с минимальной суммой расстояний


    # 📌 Алгоритм кластеризации
    while data:  # Пока есть точки
        clusters.append([data.pop()])  # Создаём новый кластер с одной случайной точкой

        for p1 in clusters[-1]:  # Проходим по точкам внутри кластера
            for p2 in data.copy():  # Проверяем все оставшиеся точки
                if dist(p1, p2) < eps:  # Если расстояние между p1 и p2 меньше порога eps
                    clusters[-1].append(p2)  # Добавляем точку p2 в текущий кластер
                    data.remove(p2)  # Удаляем p2 из общего списка точек

    # 📌 Находим центры кластеров
    c1 = [centr(cl) for cl in clusters]

    # 📌 Проверяем, что есть как минимум два кластера, чтобы избежать ошибки
    if len(c1) >= 2:
        result = (c1[0][0] + c1[1][
            0]) / 2 * 100000  # Вычисляем среднее арифметическое x-координат двух центров и масштабируем
        print(result)  # Выводим итоговый результат
    else:
        print("Недостаточно кластеров для вычислений!")

if __name__ == "__main__":
    print("Доступные примеры: primer_01, primer_02, primer_03")
    print("Вызовите нужную функцию осознанно; данные исходной задачи могут потребовать отдельного файла.")


# --- ПРОВЕРЕННЫЕ БАЗОВЫЕ БЛОКИ ---
# Только новое задание 27. По вашим файлам «27 Новое».
# В первой функции исходника return был внутри внешнего for.
# Здесь return вынесен за цикл; перебор точек и сумм расстояний сохранён.
def centr(cluster):
    if not cluster:
        raise ValueError('Пустой кластер')
    x_cent, y_cent, mini = 0, 0, 10 ** 100
    for i in range(len(cluster)):
        res = 0
        for j in range(len(cluster)):
            x1, y1 = cluster[i]
            x2, y2 = cluster[j]
            res += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        if res < mini:
            mini = res
            x_cent, y_cent = x1, y1
    return x_cent, y_cent

def svyaznye_klastery(data, eps):
    from math import dist
    data = list(data)
    clusters = []
    while data:
        clusters.append([data.pop()])
        for p1 in clusters[-1]:
            for p2 in data.copy():
                if dist(p1, p2) < eps:
                    clusters[-1].append(p2)
                    data.remove(p2)
    return clusters
