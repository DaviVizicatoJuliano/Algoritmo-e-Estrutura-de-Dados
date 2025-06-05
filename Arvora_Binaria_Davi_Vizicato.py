class NodoArvore:
    def __init__(self,dado,direita = None,esquerda = None) :
        self.dado = dado
        self.direita = direita
        self.esquerda = esquerda
        
class ArvoreBinaria:
    def __init__(self) -> None:
        self.raiz = None
        
    def inserir(self,dado):
        self.raiz = self.inserir_recursivamente(self.raiz,dado)
        
    def inserir_recursivamente(self,raiz,dado):
        if raiz is None:
            return NodoArvore(dado)
        if dado < raiz.dado:
            raiz.esquerda = self.inserir_recursivamente(raiz.esquerda,dado)
        else:
            raiz.direita = self.inserir_recursivamente(raiz.direita,dado)
        return raiz

    def procurar(self,dado):
        return self.procurar_recursivamente(self.raiz,dado)
    
    def procurar_recursivamente(self,raiz,dado):
        if raiz is None or raiz.dado == dado:
            return dado
        
        if dado < raiz.dado:
            return self.procurar_recursivamente(raiz.esquerda,dado)
        
        return self.procurar_recursivamente(raiz.direita,dado)
    
    def excluir(self, dado):
        self.raiz = self._excluir_recursivamente(self.raiz, dado)

    def _excluir_recursivamente(self, raiz, dado):
        if raiz is None:
            return raiz
        if dado < raiz.dado:
            raiz.esquerda = self._excluir_recursivamente(raiz.esquerda, dado)
        elif dado > raiz.dado:
            raiz.direita = self._excluir_recursivamente(raiz.direita, dado)
        else:
            if raiz.esquerda is None:
                return raiz.direita
            elif raiz.direita is None:
                return raiz.esquerda
            raiz.dado = self._minimo_valor_nodo(raiz.direita)
            raiz.direita = self._excluir_recursivamente(raiz.direita, raiz.dado)
        return raiz
    
    def minimo_valor(self,raiz):
        atual = raiz
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual.dado
    
    def maximo_valor(self,raiz):
        atual = raiz
        while atual.direita is not None:
            atual = atual.direita
        return atual.dado

arvore = ArvoreBinaria()

while True:
    print("\nMenu:")
    print("1. Inserir elemento")
    print("2. Buscar elemento")
    print("3. Excluir elemento")
    print("4. Sair")

    escolha = input("Escolha uma opção: ")

    match escolha:
        case "1":
            dado = int(input("Digite o valor a ser inserido: "))
            arvore.inserir(dado)
            print(f"Valor {dado} inserido com sucesso.")

        case "2":
            dado = int(input("Digite o valor a ser buscado: "))
            resultado = arvore.procurar(dado)
            if resultado:
                print(f"Valor {dado} encontrado.")
            else:
                print(f"Valor {dado} não encontrado.")

        case "3":
            dado = int(input("Digite o valor a ser excluído: "))
            arvore.excluir(dado)
            print(f"Valor {dado} excluído, se existia na árvore.")

        case "4":
            print("Saindo do programa...")
            break

        case _:
            print("Opção inválida. Tente novamente.")