from abc import ABC, abstractmethod
from typing import List

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, numbers: List[int]) -> List[int]:
        pass

class BubbleSortStrategy(SortStrategy):
    def sort(self, numbers: List[int]) -> List[int]:
        sorted_numbers = numbers.copy()
        n = len(sorted_numbers)
        for i in range(n):
            for j in range(0, n-i-1):
                if sorted_numbers[j] > sorted_numbers[j+1]:
                    sorted_numbers[j], sorted_numbers[j+1] = sorted_numbers[j+1], sorted_numbers[j]
        return sorted_numbers

class SelectionSortStrategy(SortStrategy):
    def sort(self, numbers: List[int]) -> List[int]:
        sorted_numbers = numbers.copy()
        n = len(sorted_numbers)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if sorted_numbers[min_index] > sorted_numbers[j]:
                    min_index = j
            sorted_numbers[i], sorted_numbers[min_index] = sorted_numbers[min_index], sorted_numbers[i]
        return sorted_numbers


numbers = [64, 25, 12, 22, 11]
strategy = BubbleSortStrategy()
sorted_numbers = strategy.sort(numbers)
print(sorted_numbers) 

strategy = SelectionSortStrategy()
sorted_numbers = strategy.sort(numbers)
print(sorted_numbers)