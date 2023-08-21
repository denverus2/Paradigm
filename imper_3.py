def sum_even_square(numbers):
    sum=0
    for num in numbers:
        if num % 2 == 0:
            sum=sum+num*num
    return sum


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(sum_even_square(numbers))  # Вывод: [2, 4, 6, 8]

