# Ленивые вычисления: Напишите функцию, которая будет генерировать бесконечную последовательность простых чисел. 
# Используйте ленивые вычисления, чтобы генерировать только те числа, которые действительно нужны.

def gen_primes():
  yield 2
  primes = [2]
  num = 3
  while True:
    is_prime = True
    for prime in primes:
      if prime * prime > num:
        break
      if num % prime == 0:
        is_prime = False
        break
    if is_prime:
      primes.append(num)
      yield num
    num += 2
    
primes = gen_primes()
for _ in range(9):
    print(next(primes))