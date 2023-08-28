# Декоратор:
# Создайте класс Coffee с методом cost(), возвращающим стоимость кофе. 
# Реализуйте декораторы Sugar и Milk, которые добавляют сахар и молоко к кофе, 
# соответственно. Создайте объект кофе и последовательно примените к нему декораторы, 
# затем выведите общую стоимость.

class Coffee:
    def cost(self):
        return 100.0 #Кофе за соточку

class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost()

class Sugar(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 10.0 #Сладкая жизнь + 10р

class Milk(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 10.0 #Испортить хороший кофе молоком еще десятка


coffee = Coffee()
coffee = Sugar(coffee)
coffee = Milk(coffee)
print(f'Ваш кофе {coffee.cost()}р') 