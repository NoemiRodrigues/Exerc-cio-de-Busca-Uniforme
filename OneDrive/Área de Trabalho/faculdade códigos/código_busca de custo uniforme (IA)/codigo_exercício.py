#Implemente uma busca de custo uniforme (UCS) e exiba o caminho com seu custo total.

import heapq
#importando essa biblioteca que é usada para fila de prioridades 

def exercicio_busca_de_custa_uniforme (grafo, inicio, objetivo):
#criando uma função 
    fila = [(0, [inicio])] #definindo o inicio da fila
    visitados = set()
    
    while fila:  
        custo, caminho = heapq.heappop(fila)
        #remove e retorna o menor valor da fila
        #aqui iremos remover a menor tupla (custo, caminho) da fila
        no = caminho [-1]
        if no in visitados:
            continue
        visitados.add(no)
        #marcando que já visitou 

        if no == objetivo:
            return caminho, custo

        for vizinho, custo_vizinho in grafo.get(no, []):
        #analisa os vizinhos do nó atual em que nos encontramos e o custo que seria ir até esses vizinhos
            if vizinho not in visitados:
                novo_caminho = caminho + [vizinho]
                novo_custo = custo + custo_vizinho
                heapq.heappush(fila, (novo_custo, novo_caminho))

    return None

# Exemplo de uso
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 5), ('E', 12)],
    'C': [('A', 4), ('F', 16)],
    'D': [('B', 5), ('G', 2)],
    'E': [('B', 12), ('H', 20)],
    'F': [('C', 16), ('I', 18)],
    'G': [('D', 2), ('H', 1)],
    'H': [('G', 1), ('E', 20), ('I', 2)],
    'I': [('F', 18), ('H', 2)],
}

inicio = 'A'
objetivo = 'I'
resultado = exercicio_busca_de_custa_uniforme(grafo, inicio, objetivo)

if resultado:
    caminho, custo = resultado
    print(f"Caminho: {caminho}, Custo: {custo}")
else:
    print("Caminho não encontrado.")