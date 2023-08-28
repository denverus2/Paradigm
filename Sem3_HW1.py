# Реализуйте паттерн Фабричный метод на языке Python для создания геометрических фигур.
# Создайте класс ShapeFactory, имеющий метод create_shape(), 
# который возвращает объекты различных геометрических фигур.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Рисуем круг")

class Square(Shape):
    def draw(self):
        print("Рисуем квадрат")

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type: str) -> Shape:
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        else:
            raise ValueError(f"Неизвестный тип фигуры: {shape_type}")


factory = ShapeFactory()
shape = factory.create_shape("circle")
shape.draw() 