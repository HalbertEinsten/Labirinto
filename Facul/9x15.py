from collections import deque

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])

    def is_valid_move(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols and self.maze[row][col] == 0

    def find_shortest_path(self, start, end):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        queue = deque([(start, [start])])

        while queue:
            current, path = queue.popleft()
            visited.add(current)

            if current == end:
                return path

            for dr, dc in directions:
                new_row, new_col = current[0] + dr, current[1] + dc
                if (new_row, new_col) not in visited and self.is_valid_move(new_row, new_col):
                    queue.append(((new_row, new_col), path + [(new_row, new_col)]))
                    visited.add((new_row, new_col))

        return None

    def visualize_path(self, path):
        for row in range(self.rows):
            for col in range(self.cols):
                if (row, col) in path:
                    print("*", end=" ")
                else:
                    print("#" if self.maze[row][col] == 1 else " ", end=" ")
            print()

# Exemplo de uso
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

solver = MazeSolver(maze)
start = (0, 0)
end = (4, 4)
path = solver.find_shortest_path(start, end)
if path:
    print("Caminho mais curto encontrado:")
    solver.visualize_path(path)
else:
    print("Não foi possível encontrar um caminho.")
