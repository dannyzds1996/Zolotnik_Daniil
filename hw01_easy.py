
__author__ = 'Золотник Даниил Сергеевич'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...
first = input('Введите число: ')
i = 0
while i < len(first):
    print(first[i])
    i += 1

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!
a = input('Введеите значени "a": ')
b = input('Введите значение "b": ')
c = a
a = b
b = c
print(a, "это было b")
print(b, "это было a")

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
a = int(input('Введите свой возраст: '))
if a > 18:
    print('Доступ разрещен')
else:
    print('Извините, пользование данным ресурсов только с 18 лет')