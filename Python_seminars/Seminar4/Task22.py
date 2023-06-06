# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

num1 = int(input("Введите количество элементов первого множества: "))
num2 = int(input("Введите количество элементов второго множества: "))

set1 = set([int(input(f"Введите {i + 1}-й элемент первого множества: ")) for i in range(num1)])
set2 = set([int(input(f"Введите {i + 1}-й элемент второго множества: ")) for i in range(num2)])

common_elements = sorted(set1.intersection(set2))
print("Общие элементы множеств без повторений в порядке возрастания: ", common_elements)
