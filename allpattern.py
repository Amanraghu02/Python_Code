# Right-angled triangle pattern
rows = int(input("Enter The Number for Pattern : "))
"""
for i in range(1, rows + 1):
    print("*" * i)
"""

# Inverted right-angled triangle pattern
"""
for i in range(rows, 0, -1):
    print("*" * i)
""" 

# Pyramid pattern

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))


# Diamond pattern
"""
# Upper part
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

# Lower part
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
"""

# Number triangle pattern
"""
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
""" 

"""
First row (i = 1):

Inner loop: j = 1
Output: 1
Second row (i = 2):

Inner loop: j = 1, j = 2
Output: 1 2
Third row (i = 3):

Inner loop: j = 1, j = 2, j = 3
Output: 1 2 3
Fourth row (i = 4):

Inner loop: j = 1, j = 2, j = 3, j = 4
Output: 1 2 3 4
Fifth row (i = 5):

Inner loop: j = 1, j = 2, j = 3, j = 4, j = 5
Output: 1 2 3 4 5
# Inverted number triangle pattern
"""

"""
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
"""
# Pascal's triangle pattern
"""
for i in range(rows):
    print(' ' * (rows - i), end='')

    C = 1
    for j in range(1, i + 1):
        print(C, end=' ')
        C = C * (i - j) // j
    print()
"""