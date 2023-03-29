import random

# Definir matriz inicial
matrix = [
    [3, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 4],
]

# Definir movimentos possíveis
moves = {
    'R': (0, 1),
    'L': (0, -1),
    'D': (1, 0),
    'U': (-1, 0),
}

# Função para verificar se uma célula é válida
def is_valid_cell(matrix, row, col):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return False
    return True

# Função para verificar se uma célula pode ser alcançada
def is_reachable_cell(matrix, row, col):
    if matrix[row][col] == 0 or matrix[row][col] == 4:
        return True
    return False

# Função para atualizar a matriz de acordo com as regras dadas
def update_matrix(matrix):
    new_matrix = [[0 for col in range(len(matrix[0]))] for row in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                green_neighbors = 0
                for move in moves.values():
                    new_row = row + move[0]
                    new_col = col + move[1]
                    if is_valid_cell(matrix, new_row, new_col) and matrix[new_row][new_col] == 1:
                        green_neighbors += 1
                if green_neighbors > 1 and green_neighbors < 5:
                    new_matrix[row][col] = 1
            elif matrix[row][col] == 1:
                green_neighbors = 0
                for move in moves.values():
                    new_row = row + move[0]
                    new_col = col + move[1]
                    if is_valid_cell(matrix, new_row, new_col) and matrix[new_row][new_col] == 1:
                        green_neighbors += 1
                if green_neighbors > 3 and green_neighbors < 6:
                    new_matrix[row][col] = 1
            else:
                new_matrix[row][col] = matrix[row][col]
    return new_matrix

def get_current_position(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 3:
                return i, j
    return None
            
def is_goal_reached(matrix, current_row, current_col):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 4 and row == current_row and col == current_col:
                return True
    return False

current_row, current_col = get_current_position(matrix)
path = []  # Lista para armazenar os movimentos feitos
while not is_goal_reached(matrix, current_row, current_col):
    possible_moves = []
    for move, (row, col) in moves.items():
        new_row = current_row + row
        new_col = current_col + col
        if is_valid_cell(matrix, new_row, new_col) and is_reachable_cell(matrix, new_row, new_col):
            possible_moves.append(move)
    if not possible_moves:
        print('Não é possível alcançar o objetivo.')
        break
    move = random.choice(possible_moves)
    row, col = moves[move]
    new_row = current_row + row
    new_col = current_col + col
    matrix = update_matrix(matrix)
    current_row, current_col = new_row, new_col # atualiza a posicao atual
    path.append(move)  # Adicionar o movimento feito à lista de movimentos
    for row in matrix:
        print(row)
    print('-' * 20)

# Imprimir o caminho percorrido se o objetivo for alcançado
if is_goal_reached(matrix, current_row, current_col):
    print('Objetivo alcançado! Caminho percorrido:')
    print(path)