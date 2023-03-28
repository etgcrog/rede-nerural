from queue import Queue

def read_input_file(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            row = [int(cell) for cell in line.strip().split()]
            matrix.append(row)
    return matrix

def atualiza_matriz(matriz):
    # cria uma nova matriz com as mesmas dimensões da matriz de entrada
    nova_matriz = [[0 for _ in range(len(matriz[0]))] for _ in range(len(matriz))]
    
    # percorre cada célula da matriz de entrada
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            # conta o número de células verdes adjacentes
            num_verdes = 0
            for k in range(max(i-1, 0), min(i+2, len(matriz))):
                for l in range(max(j-1, 0), min(j+2, len(matriz[0]))):
                    if (k, l) != (i, j) and matriz[k][l] == 1:
                        num_verdes += 1
            
            # aplica as regras de acordo com o estado atual da célula
            if matriz[i][j] == 0: # célula branca
                if num_verdes > 1 and num_verdes < 5:
                    nova_matriz[i][j] = 1 # célula fica verde
                else:
                    nova_matriz[i][j] = 0 # célula permanece branca
            else: # célula verde
                if num_verdes > 3 and num_verdes < 6:
                    nova_matriz[i][j] = 1 # célula permanece verde
                else:
                    nova_matriz[i][j] = 0 # célula fica branca
                    
    return nova_matriz
    
def bts(estado_inicial, regras, objetivo):
    fila = Queue()
    fila.put(estado_inicial)
    visitados = set()
    visitados.add(estado_inicial)

    while not fila.empty():
        estado_atual = fila.get()
        if estado_atual == objetivo:
            # constrói a sequência de movimentos
            movimentos = []
            while estado_atual[1] is not None:
                movimentos.append(estado_atual[1])
                estado_atual = estado_atual[0]
            movimentos.reverse()
            return ' '.join(movimentos)
        
        for novo_estado, movimento in regras(estado_atual):
            if novo_estado not in visitados:
                fila.put(novo_estado)
                visitados.add(novo_estado)
                novo_estado_pai = (estado_atual, movimento)
                
    return None

def expande_estado(estado, atualiza_matriz):
    matriz, posicao_particula = estado
    
    novos_estados = []
    i, j = posicao_particula
    
    # tenta mover para cima
    if i > 0 and matriz[i-1][j] == 0:
        nova_matriz = atualiza_matriz(matriz)
        nova_matriz[i-1][j] = 2 # marca nova posição da partícula
        novo_estado = (nova_matriz, (i-1, j))
        novos_estados.append(novo_estado)
    
    # tenta mover para baixo
    if i < len(matriz)-1 and matriz[i+1][j] == 0:
        nova_matriz = atualiza_matriz(matriz)
        nova_matriz[i+1][j] = 2 # marca nova posição da partícula
        novo_estado = (nova_matriz, (i+1, j))
        novos_estados.append(novo_estado)
    
    # tenta mover para a esquerda
    if j > 0 and matriz[i][j-1] == 0:
        nova_matriz = atualiza_matriz(matriz)
        nova_matriz[i][j-1] = 2 # marca nova posição da partícula
        novo_estado = (nova_matriz, (i, j-1))
        novos_estados.append(novo_estado)
    
    # tenta mover para a direita
    if j < len(matriz[0])-1 and matriz[i][j+1] == 0:
        nova_matriz = atualiza_matriz(matriz)
        nova_matriz[i][j+1] = 2 # marca nova posição da partícula
        novo_estado = (nova_matriz, (i, j+1))
        novos_estados.append(novo_estado)
    
    return novos_estados



matriz_inicial = read_input_file('stone-challenge\input.txt')
matriz_final = read_input_file('stone-challenge\output.txt')
posicao_particula = None

# adiciona a posição inicial da partícula ao estado inicial
estado_inicial = (matriz_inicial, posicao_particula, None)

# regras de transição
regras = lambda estado: expande_estado(estado, atualiza_matriz)

# estado objetivo
objetivo = (matriz_final, None, None)

# encontra a sequência de movimentos
movimentos = bts(estado_inicial, regras, objetivo)

# imprime a sequência de movimentos
print(movimentos)

