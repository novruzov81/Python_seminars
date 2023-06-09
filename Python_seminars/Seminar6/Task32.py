# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def find_indexes(lst, min_val, max_val):
    indexes = []
    for i in range(len(lst)):
        if min_val <= lst[i] <= max_val:
            indexes.append(i)
    return indexes

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
indexes = find_indexes(my_list, 3, 7)
print(indexes)
