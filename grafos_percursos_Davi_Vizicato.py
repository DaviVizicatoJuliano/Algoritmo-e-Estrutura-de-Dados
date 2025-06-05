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
            
    def busca_profundidade(self, inicio, visitados=None):
        if visitados is None:
            visitados = set()
        visitados.add(inicio)
        print(inicio, end=' -> ')
        
        for vizinho, peso in self.adjacencia[inicio]:
            if vizinho not in visitados:
                self.busca_profundidade(vizinho, visitados)
                
    def busca_largura(self, inicio):
        visitado = set()
        fila = [inicio]
        visitado.add(inicio)
        
        while fila:
            vertice = fila.pop(0)
            print(vertice, end=' -> ')
            
            for vizinho, peso in self.adjacencia[vertice]: 
                if vizinho not in visitado:
                    visitado.add(vizinho)
                    fila.append(vizinho)

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

grafo = CidadesNaoDirecionadas()

grafo.adicionar_local("Drogasil")
grafo.adicionar_local("Colegio Objetivo")
grafo.adicionar_local("Restaurante Maria Fumaça")
grafo.adicionar_local("Bar do Mineiro")
grafo.adicionar_local("Escola Municipal Gomes da Silva")
grafo.adicionar_local("Supermercado Central")
grafo.adicionar_local("Parque da Cidade")
grafo.adicionar_local("Hospital São Lucas")
grafo.adicionar_local("Biblioteca Pública")
grafo.adicionar_local("Estação Rodoviária")

grafo.adicionar_rua("Drogasil", "Restaurante Maria Fumaça",1)
grafo.adicionar_rua("Drogasil", "Bar do Mineiro",2)
grafo.adicionar_rua("Drogasil", "Escola Municipal Gomes da Silva",2)
grafo.adicionar_rua("Drogasil", "Colegio Objetivo",4)
grafo.adicionar_rua("Restaurante Maria Fumaça", "Parque da Cidade",10)
grafo.adicionar_rua("Bar do Mineiro", "Supermercado Central",4)
grafo.adicionar_rua("Supermercado Central", "Hospital São Lucas",6)
grafo.adicionar_rua("Hospital São Lucas", "Estação Rodoviária",7)
grafo.adicionar_rua("Parque da Cidade", "Estação Rodoviária",8)
grafo.adicionar_rua("Colegio Objetivo", "Parque da Cidade", 6)
grafo.adicionar_rua("Supermercado Central", "Biblioteca Pública", 2)
grafo.adicionar_rua("Biblioteca Pública", "Estação Rodoviária", 3)


grafo.exibir_rota()
print("Busca por Largura")
grafo.busca_largura("Drogasil")
print("\n")
print("Busca por profundidade")
grafo.busca_profundidade("Drogasil")
print("\n")
print("Prim")
print(grafo.prim())
print("\n")
print("Kruskal")
print(grafo.kruskal())