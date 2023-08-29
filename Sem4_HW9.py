# Функции высшего порядка: Создайте функцию высшего порядка, которая принимает другую функцию и список чисел.
# Функция высшего порядка должна возвращать список, содержащий результаты применения переданной функции к каждому элементу списка.

def apply_function(f, numbers):
  return [f(x) for x in numbers]

def square(x):
  return x * x

numbers = [1, 2, 3, 4]
squared_numbers = apply_function(square, numbers)
print(squared_numbers)