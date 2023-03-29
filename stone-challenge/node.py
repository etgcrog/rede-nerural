import heapq

def manhattan_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def a_star(pos_inicial, pos_final, heuristica, acoes_possiveis, custo_acao, matriz):
    fila = []
    heapq.heappush(fila, (0, pos_inicial))
    visitados = set()
    caminho = {}
    g_score = {pos_inicial: 0}
    f_score = {pos_inicial: heuristica(pos_inicial, pos_final)}

    while fila:
        _, pos_atual = heapq.heappop(fila)

        if pos_atual == pos_final:
            path = []
            while pos_atual in caminho:
                path.append(pos_atual)
                pos_atual = caminho[pos_atual]
            return path[::-1]

        visitados.add(pos_atual)

        for dx, dy in acoes_possiveis:
            nova_pos = (pos_atual[0] + dx, pos_atual[1] + dy)
            if 0 <= nova_pos[0] < len(matriz) and 0 <= nova_pos[1] < len(matriz[0]) and nova_pos not in visitados:
                g_nova = g_score[pos_atual] + custo_acao
                if nova_pos not in g_score or g_nova < g_score[nova_pos]:
                    caminho[nova_pos] = pos_atual
                    g_score[nova_pos] = g_nova
                    f_score[nova_pos] = g_nova + heuristica(nova_pos, pos_final)
                    heapq.heappush(fila, (f_score[nova_pos], nova_pos))

    return None

def main():
    matriz_final = [
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    pos_inicial = (0, 0)
    pos_final = (5, 5)
    acoes_possiveis = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    custo_acao = 1

    caminho = a_star(pos_inicial, pos_final, manhattan_distance, acoes_possiveis, custo_acao, matriz_final)

    if caminho:
        print("Caminho encontrado:")
        for pos in caminho:
            print(pos)
    else:
        print("Não foi possível encontrar um caminho.")

if __name__ == "__main__":
    main()
