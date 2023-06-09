# Напишите функцию same_by(characteristic, objects), которая проверяет,
# все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов,
# функция должна возвращать True.
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.

def same_by(characteristic, objects):
    if not objects:
        return True
    characteristic_values = set()
    for obj in objects:
        characteristic_values.add(characteristic(obj))
        if len(characteristic_values) > 1:
            return False
    return True