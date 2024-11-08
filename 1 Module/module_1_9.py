example = 'Топинамбур'
print(example[0])
print(example[-1])
print(example[5:])
print(example[::-1])
print(example[1::2])



# Теория
# [0:3] - : значит диапозон от - до
# [0:3:2] - : значит диапозон от - до с шагом 2
# [:3] - : значит диапозон с начала до 3
# [2:] - : значит диапозон с 2 до конца
# [::2] - : значит диапозон шаг 2

"""
Цель: Научиться работать со строками и индексацией строк в Python.
Задача:
Выполните следующие действия в PyCharm:
В переменную example запишите любую строку.
Выведите на экран(в консоль) первый символ этой строки.
Выведите на экран(в консоль) последний символ этой строки (используя отрицательный индекс).
Выведите на экран(в консоль) вторую половину этой строки (С нечётным количеством символов: 'Urban' -> 'ban').
Выведите на экран(в консоль) это слово наоборот.
Выведите на экран(в консоль) каждый второй символ этой строки. (Пример: 'Топинамбур'->'оиабр')
Вводные данные:
example = 'Топинамбур'
Вывод на экран(в консоль):
Т
р
амбур
рубманипоТ
оиабр
Примечания:
Для вывода значений на экран используйте функцию print()
Для доступа к символу строки по индексу используйте квадратные скобки и индекс символа ('Urban'[3] -  четвёртый символ строки 'Urban' - 'a')
Индексация начинается с нуля.
"""