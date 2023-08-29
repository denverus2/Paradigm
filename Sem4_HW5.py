# Замыкание: Создайте функцию, которая принимает некоторое число n и возвращает функцию, 
# которая прибавляет n к своему аргументу. Продемонстрируйте использование этой функции-замыкания.

def create_adder(n):
  def adder(x):
    return x + n
  return adder
  
add_five = create_adder(5)
result = add_five(3)
print(result)