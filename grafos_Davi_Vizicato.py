import heapq

class CidadesNaoDirecionadas:
    def __init__(self):
        self.adjacencia = {}
        self.arestas = []
        
    def adicionar_local(self, local):
        if local not in self.adjacencia:
            self.adjacencia[local] = []
            
    def adicionar_rua(self, origem, destino, peso):
        if origem in self.adjacencia and destino in self.adjacencia:
            self.adjacencia[origem].append((destino, peso))
            self.adjacencia[destino].append((origem, peso))
            self.arestas.append((peso, origem, destino))
            
    def exibir_rota(self):
        for rua, vizinhos in self.adjacencia.items():
            rotas = ", ".join([f"{destino} (peso: {peso})" for destino, peso in vizinhos])
            print(f"{rua} -> {rotas}")
            
    def prim(self):
        if not self.adjacencia:
            return []
        
        inicio = next(iter(self.adjacencia))
        mst = []
        visitado = set()
        heap = [(0, inicio, None)]
        
        while heap:
            peso, vertice, origem = heapq.heappop(heap)
            if vertice not in visitado:
                visitado.add(vertice)
                if origem is not None:
                    mst.append((origem, vertice, peso))
                
                for vizinho, custo in self.adjacencia[vertice]:
                    if vizinho not in visitado:
                        heapq.heappush(heap, (custo, vizinho, vertice))
        
        return mst
    
    def kruskal(self):
        def find(pai, vertice):
            if pai[vertice] != vertice:
                pai[vertice] = find(pai, pai[vertice])
            return pai[vertice]
        
        def union(pai, rank, v1, v2):
            raiz1 = find(pai, v1)
            raiz2 = find(pai, v2)
            
            if raiz1 != raiz2:
                if rank[raiz1] > rank[raiz2]:
                    pai[raiz2] = raiz1
                elif rank[raiz1] < rank[raiz2]:
                    pai[raiz1] = raiz2
                else:
                    pai[raiz2] = raiz1
                    rank[raiz1] += 1
            
        self.arestas.sort()
        pai = {vertice: vertice for vertice in self.adjacencia}
        rank = {vertice: 0 for vertice in self.adjacencia}
        mst = []
        
        for peso, v1, v2 in self.arestas:
            if find(pai, v1) != find(pai, v2):
                union(pai, rank, v1, v2)
                mst.append((v1, v2, peso))
        
        return mst

    def bfs(self, inicio):
        visitado = set()
        fila = [inicio]
        visitado.add(inicio)
        caminho = {inicio: None}  # Dicionário para rastrear o caminho

        while fila:
            vertice = fila.pop(0)
            print(vertice, end=" ")  # Visita o vértice
            
            for vizinho, _ in self.adjacencia[vertice]:
                if vizinho not in visitado:
                    visitado.add(vizinho)
                    fila.append(vizinho)
                    caminho[vizinho] = vertice  # Guarda o pai do vértice

        return caminho

    def dfs(self, inicio, visitado=None):
        if visitado is None:
            visitado = set()
        if inicio not in visitado:
            print(inicio, end=" ")  # Visita o vértice
            visitado.add(inicio)
            for vizinho, _ in self.adjacencia[inicio]:
                self.dfs(vizinho, visitado)

grafo = CidadesNaoDirecionadas()

grafo.adicionar_local("A")
grafo.adicionar_local("B")
grafo.adicionar_local("C")
grafo.adicionar_local("D")
grafo.adicionar_local("E")

grafo.adicionar_rua("A", "C", 3)
grafo.adicionar_rua("B", "E", 2)
grafo.adicionar_rua("C", "E", 6)
grafo.adicionar_rua("D", "A", 9)
grafo.adicionar_rua("E", "A", 1)
grafo.adicionar_rua("C", "B", 2)
grafo.adicionar_rua("D", "C", 7)

'''grafo.adicionar_rua("A", "B", 4)
grafo.adicionar_rua("A", "E", 7)
grafo.adicionar_rua("B", "C", 5)
grafo.adicionar_rua("B", "D", 10)
grafo.adicionar_rua("C", "D", 3)
grafo.adicionar_rua("D", "E", 8)'''

print("Rotas do grafo:")
grafo.exibir_rota()

print("\nÁrvore Geradora Mínima (Prim):")
print(grafo.prim())

print("\nÁrvore Geradora Mínima (Kruskal):")
print(grafo.kruskal())

print("\nBusca em Largura (BFS) a partir de A:")
grafo.bfs("A")

print("\n\nBusca em Profundidade (DFS) a partir de A:")
grafo.dfs("A")