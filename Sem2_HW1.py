# Задание: Создайте функцию, которая принимает двумерный массив (лабиринт) и начальную и конечную точки. Функция должна возвращать путь от начальной до конечной точки или сообщение, что путь невозможен.
# Входные данные:
# Двумерный массив размера MxN, где '0' - это проход, а '1' - это стена.
# Координаты начальной и конечной точки.
# Выходные данные:
# Массив координат пути или сообщение об ошибке.
# **Процедурное программирование:

# Разбиение массива на подмассивы:**


from collections import deque

def find_path(maze, start, end):
    queue = deque([start])
    visited = set([start])
    parents = {start: None}

    while queue:
        current = queue.popleft()
        if current == end:
            path = []
            while current is not None:
                path.append(current)
                current = parents[current]
            return list(reversed(path))
        row, col = current
        neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        for neighbor in neighbors:
            n_row, n_col = neighbor
            if n_row < 0 or n_row >= len(maze) or n_col < 0 or n_col >= len(maze[0]):
                continue
            if maze[n_row][n_col] == 1:
                continue
            if neighbor in visited:
                continue
            visited.add(neighbor)
            queue.append(neighbor)
            parents[neighbor] = current

    return "Путь не найден"

maze = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0],
]

start = (0, 0)
end = (3, 3)

path = find_path(maze, start, end)
print(path)