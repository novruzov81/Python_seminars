# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в
# массиве A[1..N]. Пользователь в первой строке вводит натуральное число
# N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint
spis = list()
count = int(input("Введите количество элементов: "))
num = int(input("Введите искомое число: "))
for i in range(count):
    spis.append(randint(0, 10))
print(spis)
numbers = 0
for i in range(len(spis)):
    if spis[i] == num:
        numbers+=1
print("Количество элементов", num, "=", numbers)