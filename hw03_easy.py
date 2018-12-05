# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def f(n=float(input("Введите число: "))):
    if float(n) - int(n) > 0.5:
        print(int(n) + 1)
    else:
        print(int(n))
f()

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
def lucky_number():
    biletik = input("Введите номер билета из 6 цифр: ")
    numbers = list(biletik)
    numbers = [int(i) for i in numbers]
    if (sum(numbers[:3]) == sum(numbers[3:])):
        print("Счастливый")
    else:
        print("Обычный")

lucky_number()