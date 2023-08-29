# Функции-редуцеры для списков: Напишите функцию-редуктор, которая принимает список строк и возвращает строку, 
# состоящую из объединенных элементов списка через запятую. 
# Например, для списка ["apple", "banana", "cherry"] результат должен быть "apple, banana, cherry".

from functools import reduce

def join_strings(strings):
  return reduce(lambda x, y: x + ', ' + y, strings)

sp = ["apple", "banana", "cherry"]
print(join_strings(sp))
