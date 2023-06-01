# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество
# элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка
# содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint
spis = list()
count = int(input("Введите количество элементов: "))
for i in range(count):
    spis.append(randint(1, 10))
print(spis)
num = int(input("Введите искомое число: "))
temp = spis[0]
for i in range(count):
    if abs(spis[i] -count) < abs(temp - count):
        temp = spis[i]
print("Самый близкий к заданному числу элемент - ", temp)