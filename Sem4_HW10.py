# Чистые функции и неизменяемость данных: Напишите функцию, которая принимает список чисел и возвращает новый список, 
# в котором каждый элемент умножен на 2. Убедитесь, что вы используете только чистые функции и не изменяете исходный список.

def double(numbers):
    return [x * 2 for x in numbers]
  
  
numbers = [1, 2, 3, 4]
print (numbers)
print(double(numbers))
print (numbers)