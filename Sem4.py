# def square(x):
#     return x * x

# # Присвоение функции square переменной func
# func = square 

# # Теперь переменная func содержит функцию square
# result = func(5)
# print(result)  # Вывод: 25

# def apply_function(func, x):
#     return func(x)

# def double(x):
#     return x * 2

# def triple(x):
#     return x * 3

# result1 = apply_function(double, 5)
# result2 = apply_function(triple, 5)

# print(result1)  # Вывод: 10
# print(result2)  # Вывод: 15

# def create_multiplier(factor):
#     def multiplier(x):
#         return x * factor
#     return multiplier

# double = create_multiplier(2)
# triple = create_multiplier(3)

# result1 = double(5)
# result2 = triple(5)

# print(result1)  # Вывод: 10
# print(result2)  # Вывод: 15

# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# function_list = [add, subtract]

# result1 = function_list[0](5, 3)
# result2 = function_list[1](10, 4)

# print(result1)  # Вывод: 8
# print(result2)  # Вывод: 6


# # Пример изменяемых данных
# mutable_list = [1, 2, 3]
# mutable_list[1] = 10  # Изменение элемента списка

# # Пример неизменяемых данных
# immutable_tuple = (1, 2, 3)
# new_tuple = immutable_tuple + (10,)  # Создание нового кортежа на основе старого
# def append_to_list(lst, item):
#     """
#     Создает новый список, добавляя элемент к существующему списку.

#     :param lst: Исходный список.
#     :param item: Элемент для добавления.
#     :return: Новый список с добавленным элементом.
#     """
#     return lst + [item]  # Создание нового списка на основе старого

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# result = factorial(5)
# print(result)  # Выведет: 120

# def sum_list(numbers):
#     if not numbers:
#         return 0
#     else:
#         return numbers[0] + sum_list(numbers[1:])

# numbers = [1, 2, 3, 4, 5]
# result = sum_list(numbers)
# print(result)  # Выведет: 15

# def sum_list(numbers):
#     return sum(numbers)

# numbers = [1, 2, 3, 4, 5]
# total = sum_list(numbers)
# print(total)  # Выведет: 15


# def apply_function(func, numbers):
#     return [func(x) for x in numbers]

# def square(x):
#     return x ** 2

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = apply_function(square, numbers)
# print(squared_numbers)  # Выведет: [1, 4, 9, 16, 25]

# def custom_sort(numbers, comparison_func):
#     return sorted(numbers, key=comparison_func)

# def descending_order(x):
#     return -x

# numbers = [5, 2, 8, 1, 9, 3]
# sorted_numbers = custom_sort(numbers, descending_order)
# print(sorted_numbers)  # Выведет: [9, 8, 5, 3, 2, 1]

# def outer_function(x):
#     def inner_function(y):
#         return x + y
#     return inner_function

# add_five = outer_function(5)
# result = add_five(10)  # Замыкание захватывает x = 5
# print(result)  # Выведет: 15

# def counter():
#     count = 0
#     def increment():
#         nonlocal count  # Используется nonlocal для изменения переменной из внешней области
#         count += 1
#         return count
#     return increment

# counter_func = counter()
# print(counter_func())  # Выведет: 1
# print(counter_func())  # Выведет: 2
# print(counter_func())  # Выведет: 3

# def make_multiplier(factor):
#     def multiplier(number):
#         return number * factor
#     return multiplier

# double = make_multiplier(2)
# triple = make_multiplier(3)

# print(double(5))  # Выведет: 10
# print(triple(5))  # Выведет: 15

# def sum_reducer(acc, value):
#     return acc + value

# numbers = [1, 2, 3, 4, 5]
# result = reduce(sum_reducer, numbers, 0)
# print(result)  # Выведет: 15


# def max_reducer(acc, value):
#     return max(acc, value)

# numbers = [12, 34, 25, 45, 60]
# result = reduce(max_reducer, numbers)
# print(result)  # Выведет: 60


# def concat_reducer(acc, value):
#     return acc + value

# strings = ["Hello, ", "world", "!", " Welcome"]
# result = reduce(concat_reducer, strings)
# print(result)  # Выведет: "Hello, world! Welcome"

# class Maybe:
#     def __init__(self, value):
#         self.value = value

#     def bind(self, func):
#         if self.value is None:
#             return self
#         return func(self.value)

# # Пример использования
# def safe_divide(x):
#     if x == 0:
#         return Maybe(None)
#     return Maybe(10 / x)

# result = Maybe(5).bind(safe_divide)
# print(result.value)  # Выведет: 2.0

# result = Maybe(0).bind(safe_divide)
# print(result.value)  # Выведет: None

# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b

# fib = fibonacci()
# fib2=fibonacci()

# for _ in range(10):
#     print(next(fib))

# print(111, next(fib))
# print(111, next(fib2))