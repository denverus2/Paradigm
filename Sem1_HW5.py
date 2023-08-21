# Задача 5: Поиск простых чисел. Напишите программу, которая находит все простые числа в заданном диапазоне от 1 до N.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find_primes(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

n = int(input("Введите число N: "))
print("Простые числа в диапазоне от 1 до", n, ":", find_primes(n))