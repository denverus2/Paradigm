# Задача 1: Напишите программу, которая находит все простые числа в заданном диапазоне.


def primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes

start = 10
end = 30
print(primes_in_range(start, end))