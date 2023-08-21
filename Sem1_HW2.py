# Задача 2: Поиск наименьшего числа в списке. Напишите программу, которая находит наименьшее число в заданном списке с помощью цикла.

def find_minimum_number(list):
    min_num = list[0]
    for i in range(1, len(list)):
        if list[i] < min_num:
            min_num = list[i]
    return min_num

i=[3, 5, 1, 7]
print(find_minimum_number(i))