# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
import random
print("Задание №1: ")
kv = [random.randint(1,10) for _ in range(4)]
print("Исходный список: ", kv)
kvadrat_kv = list(map(lambda x:x**2, kv))
print("Конечный список: ", kvadrat_kv)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
print("Задание №2: ")
fruits1 = ["яблоко", "груша", "абрикос", "персик", "мандарин"]
print("Список фруктов №1: ", fruits1)
fruits2 = ["яблоко", "груша", "абрикос", "банан", "апельсин"]
print("Список фруктов №2: ", fruits2)
fruitsall = [i for i in fruits1 if i in fruits2]
print("Пересечение списков: ", fruitsall)


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
import random
print("Задание №3: ")
list1 = [random.randint(-20, 20) for _ in range(20)]
print("Исходный список: ", list1)
list2 = [i for i in list1 if  not i % 3 and i > 0 and i % 4]
print("Конечный список: ", list2)