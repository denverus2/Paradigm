# Задание: Напишите функцию, которая принимает массив чисел и значение X. Функция должна возвращать массив подмассивов так, чтобы сумма чисел в каждом подмассиве была меньше или равна X.
# Входные данные:
# Массив чисел длиной N.
# Число X.
# Выходные данные:
# Массив подмассивов.


def split_array(arr, x):
    subarrays = []
    subarray = []
    for num in arr:
        if sum(subarray) + num > x:
            if subarray:
                subarrays.append(subarray)
            subarray = []
        subarray.append(num)
    if subarray:
        subarrays.append(subarray)
    return [subarray for subarray in subarrays if sum(subarray) <= x]

arr = [1, 2, 3, 4, 5]
x = 3

result = split_array(arr, x)
print(result)