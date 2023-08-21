# Задача 6: Упорядочивание списка. Напишите программу, которая сортирует список чисел в порядке возрастания с использованием пузырьковой сортировки или другого метода сортировки.

def sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
sort(arr)
print("Отсортированный список:", arr)