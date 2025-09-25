rows, cols = 7, 7
matrix = [[1 if j % 2 == 0 else 0 for j in range(cols)] for _ in range(rows)]

for row in matrix:
    print(''.join(map(str, row)))