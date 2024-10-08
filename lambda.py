add = lambda x, y: x + y
print(add(3, 5))  # Output: 8

points = [(1, 2), (3, 1), (5, 7), (2, 3)]
points.sort(key=lambda x: x[1])  # Sort by second value in each tuple
print(points)
# Output: [(3, 1), (1, 2), (2, 3), (5, 7)]

nums = [1, 2, 3, 4]
squares = map(lambda x: x ** 2, nums)  # Squaring each number
print(list(squares))  # Output: [1, 4, 9, 16]
