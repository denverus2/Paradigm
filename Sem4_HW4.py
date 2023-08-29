# Функция-редуктор: Напишите функцию-редуктор (или функцию свертки), которая принимает начальное значение и список чисел, 
# а затем возвращает произведение всех чисел в списке. Используйте эту функцию для вычисления произведения чисел в списке.

from functools import reduce

def product(numbers: list, initial):
  return reduce(lambda x, y: x * y, numbers, initial)
  
  
numbers = [1, 2, 3, 4]
print (product([1, 2, 3, 4], 1))