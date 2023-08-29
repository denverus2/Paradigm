# Рекурсивная сумма: Напишите рекурсивную функцию, которая вычисляет сумму всех чисел от 1 до n. 
# Например, для n = 5 результат должен быть 1 + 2 + 3 + 4 + 5 = 15.

def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n - 1)
      
print (recursive_sum(5))