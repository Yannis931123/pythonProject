# # 创建两个集合，并计算它们的交集和并集
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# intersection = set1 & set2
# union = set1 | set2
# print("Intersection:", intersection)
# print("Union:", union)

# # 打印前10个斐波那契数列
# def fibonacci(n):
#     fib_sequence = [0, 1]
#     for i in range(2, n):
#         fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
#     return fib_sequence[:n]
#
# print(fibonacci(10))

# # 创建一个生成器，生成1到10的数字
# def number_generator(n):
#     for i in range(1, n + 1):
#         yield i
#
# gen = number_generator(20)
# for num in gen:
#     print(num)

# # 写入数据到文件，并读取文件内容
# with open("../testdata/example.txt", "w") as file:
#     file.write("Hello, World!\n")
#
# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)


import heapq


class Node:
    def __init__(self, position, parent=None, cost=0, heuristic=0):
        self.position = position
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return self.cost + self.heuristic < other.cost + other.heuristic


def a_star(maze, start, end):
    open_set = []
    heapq.heappush(open_set, Node(start, None, 0, heuristic(start, end)))
    closed_set = set()
    came_from = {}

    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while open_set:
        current = heapq.heappop(open_set)

        if current.position == end:
            path = []
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        closed_set.add(current.position)

        for neighbor, cost in get_neighbors(maze, current.position):
            if neighbor in closed_set:
                continue

            tentative_g_score = g_score[current.position] + cost

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                heapq.heappush(open_set,
                               Node(neighbor, current, tentative_g_score, f_score[neighbor] - tentative_g_score))

    return None


# Heuristic function (e.g., Manhattan distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# Get neighbors for a given position in the maze
def get_neighbors(maze, position):
    # Simplified for a 4-connected grid (up, down, left, right)
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = position
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
            neighbors.append(((nx, ny), 1))  # Assuming uniform cost of 1 for moving between adjacent cells
    return neighbors


# Example usage:
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
end = (4, 4)
path = a_star(maze, start, end)
print(path)  # Output the path found by A*
