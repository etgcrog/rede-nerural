import queue

moves = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

def is_valid_cell(matrix, row, col):
    """
    Checa se uma célula é válida na matriz.
    """
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row][col] != -1

def bfs(matrix, start_row, start_col, goal_row, goal_col):
    """
    Executa uma busca em largura para encontrar o menor caminho na matriz entre dois pontos.
    """
    q = queue.Queue()
    visited = set()
    path = []

    q.put((start_row, start_col, path))
    visited.add((start_row, start_col))

    while not q.empty():
        current_row, current_col, path = q.get()
        if current_row == goal_row and current_col == goal_col:
            return path
        for move, (delta_row, delta_col) in moves.items():
            new_row = current_row + delta_row
            new_col = current_col + delta_col
            if (new_row, new_col) not in visited and is_valid_cell(matrix, new_row, new_col):
                new_path = path.copy()
                new_path.append(move)
                q.put((new_row, new_col, new_path))
                visited.add((new_row, new_col))

    return None


def is_goal_reached(matrix, current_row, current_col):
    """
    Checa se o objetivo foi alcançado (o robô chegou à célula final) em uma determinada posição.
    """
    return matrix[current_row][current_col] == 4

def update_matrix(matrix):
    """
    Atualiza a matriz de acordo com as regras de propagação.
    """
    new_matrix = [[0 for col in range(len(matrix[0]))] for row in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            green_neighbors = 0
            for delta_row, delta_col in moves.values():
                new_row = row + delta_row
                new_col = col + delta_col
                if is_valid_cell(matrix, new_row, new_col) and matrix[new_row][new_col] == 1:
                    green_neighbors += 1
            if matrix[row][col] == 0:
                if green_neighbors > 1 and green_neighbors < 5:
                    new_matrix[row][col] = 1
            else: # matrix[row][col] == 1
                if green_neighbors > 3 and green_neighbors < 6:
                    new_matrix[row][col] = 1
    return new_matrix

def run_bfs(matrix, start_row, start_col, goal_row, goal_col):
    """
    Executa o algoritmo BTS.
    """
    path = []
    current_row, current_col = start_row, start_col
    while not is_goal_reached(matrix, current_row, current_col):
        shortest_path = bfs(matrix, current_row, current_col, goal_row, goal_col)
        if shortest_path is None:
            break
        path.extend(shortest_path)
        
        # Update the current position
        for move in shortest_path:
            delta_row, delta_col = moves[move]
            current_row += delta_row
            current_col += delta_col

            matrix = update_matrix(matrix)

    return path

matrix = [    
    [3, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 4]
]

start_row, start_col = 0, 0
goal_row, goal_col = 6, 7

path = run_bfs(matrix, start_row, start_col, goal_row, goal_col)
print(path)