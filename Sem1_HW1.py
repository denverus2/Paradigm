# Задача 1: Подсчет суммы четных чисел от 1 до N. Напишите программу, используя цикл, которая находит сумму всех четных чисел в диапазоне от 1 до заданного числа N.

def sum_of_even_numbers(n):
    sum = 0
    for i in range(2, n+1, 2):
        sum += i
    return sum

n=10
print(sum_of_even_numbers(n))