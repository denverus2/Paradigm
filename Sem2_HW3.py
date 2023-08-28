# Задание: Напишите рекурсивную функцию для вычисления n-того числа Фибоначчи.
# Входные данные:
# Число n.
# Выходные данные:
# n-тое число Фибоначчи.



def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 9

result = fibonacci(n)
print(result)