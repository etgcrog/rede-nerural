def count_green_neighbors(matrix, i, j):
    green_count = 0
    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    for dr, dc in directions:
        row, col = i + dr, j + dc

        if 0 <= row < rows and 0 <= col < cols and matrix[row][col] == 1:
            green_count += 1

    return green_count

matrix = [
    [3, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 4],
]

new_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

temp_matrix = matrix.copy()

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        cell = temp_matrix[i][j]
        green_neighbors = count_green_neighbors(temp_matrix, i, j)

        if cell == 0:
            if green_neighbors > 1 and green_neighbors < 5:
                new_matrix[i][j] = 1
            else:
                new_matrix[i][j] = 0
        elif cell == 1:
            if green_neighbors > 3 and green_neighbors < 6:
                new_matrix[i][j] = 1
            else:
                new_matrix[i][j] = 0
        else:
            new_matrix[i][j] = temp_matrix

