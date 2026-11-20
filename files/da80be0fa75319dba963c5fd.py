# -*- coding: utf-8 -*-



# --- ПРОВЕРЕННЫЕ БАЗОВЫЕ БЛОКИ ---
# Восстановлено по скриншотам сортировки и расписания.
# Начальные данные передаются аргументом: не привязаны к старому пути файла.
def raspisanie(a):
    a = sorted(a, key=lambda x: x[1])
    t = []
    for interval in a:
        if not t or interval[0] >= t[-1][1]:
            t.append(interval)
    return t

def sortirovka_dvuh_stolbcov(matrix):
    return sorted(matrix, key=lambda x: (x[0], x[1]))
