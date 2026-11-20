# -*- coding: utf-8 -*-


# --- ПРОВЕРЕННЫЕ БАЗОВЫЕ БЛОКИ ---
# По снимку «ещё/6/ЕГЭ Задание 6.docx», второй пример.
# Подсказки редактора к аргументам убраны; команды и коэффициент сохранены.
# Вызов открывает окно рисунка. Сам по себе импорт файла его не открывает.
def chertezhnik(k=15):
    from turtle import screensize, tracer, left, right, goto, xcor, ycor, up, dot, done
    screensize(5000, 5000)
    tracer(0)
    left(90)
    right(30)
    for _ in range(7):
        goto(xcor() + 6 * k, ycor() - 9 * k)
        goto(xcor() - 16 * k, ycor() + 2 * k)
        goto(xcor() + 12 * k, ycor() + 3 * k)
    up()
    for x in range(-k * 5, k * 5):
        for y in range(-k * 5, k * 5):
            goto(x * k, y * k)
            dot(5, 'red')
    done()
