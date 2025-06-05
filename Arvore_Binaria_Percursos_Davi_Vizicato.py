class NodoArvore:
    def __init__(self, dado, direita=None, esquerda=None):
        self.dado = dado
        self.direita = direita
        self.esquerda = esquerda


class ArvoreBinaria:
    def __init__(self) -> None:
        self.raiz = None

    def inserir(self, dado):
        self.raiz = self.inserir_recursivamente(self.raiz, dado)

    def inserir_recursivamente(self, raiz, dado):
        if raiz is None:
            return NodoArvore(dado)
        if dado < raiz.dado:
            raiz.esquerda = self.inserir_recursivamente(raiz.esquerda, dado)
        else:
            raiz.direita = self.inserir_recursivamente(raiz.direita, dado)
        return raiz

    def procurar(self, dado):
        return self.procurar_recursivamente(self.raiz, dado)

    def procurar_recursivamente(self, raiz, dado):
        if raiz is None:
            return False
        if raiz.dado == dado:
            return True
        if dado < raiz.dado:
            return self.procurar_recursivamente(raiz.esquerda, dado)
        return self.procurar_recursivamente(raiz.direita, dado)

    def excluir(self, dado):
        if not self.procurar(dado):
            print(f"O valor {dado} não pode ser apagado porque não existe.")
            return
        self.raiz = self.excluir_recursivamente(self.raiz, dado) 
        print(f"O valor {dado} foi excluído.")

    def excluir_recursivamente(self, raiz, dado):
        if raiz is None:
            return raiz

        if dado < raiz.dado:
            raiz.esquerda = self.excluir_recursivamente(raiz.esquerda, dado)
        elif dado > raiz.dado:
            raiz.direita = self.excluir_recursivamente(raiz.direita, dado)
        else:

            if raiz.esquerda is None:
                return raiz.direita
            elif raiz.direita is None:
                return raiz.esquerda

            raiz.dado = self.minimo_valor(raiz.direita)
            raiz.direita = self.excluir_recursivamente(raiz.direita, raiz.dado)
        return raiz

    def minimo_valor(self, raiz):
        atual = raiz
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual.dado

    def maximo_valor(self, raiz):
        atual = raiz
        while atual.direita is not None:
            atual = atual.direita
        return atual.dado

    def pre_ordem(self, raiz):
        if raiz:
            print(raiz.dado, end=" ")
            self.pre_ordem(raiz.esquerda)
            self.pre_ordem(raiz.direita)

    def em_ordem(self, raiz):
        if raiz:
            self.em_ordem(raiz.esquerda)
            print(raiz.dado, end=" ")
            self.em_ordem(raiz.direita)

    def pos_ordem(self, raiz):
        if raiz:
            self.pos_ordem(raiz.esquerda)
            self.pos_ordem(raiz.direita)
            print(raiz.dado, end=" ")

    def nivel_ordem(self):
        if self.raiz is None:
            return
        fila = [self.raiz]
        while fila:
            atual = fila.pop(0)
            print(atual.dado, end=" ")
            if atual.esquerda:
                fila.append(atual.esquerda)
            if atual.direita:
                fila.append(atual.direita)

arvore = ArvoreBinaria()

while True:
    print("\nMenu:")
    print("1. Inserir elemento")
    print("2. Buscar elemento")
    print("3. Excluir elemento")
    print("4. Percursos da árvore")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")

    match escolha:
        case "1":
            dado = int(input("Digite o valor a ser inserido: "))
            arvore.inserir(dado)
            print(f"Valor {dado} inserido com sucesso.")

        case "2":
            dado = int(input("Digite o valor a ser buscado: "))
            if arvore.procurar(dado):
                print(f"Valor {dado} encontrado.")
            else:
                print(f"Valor {dado} não encontrado.")

        case "3":
            dado = int(input("Digite o valor a ser excluído: "))
            arvore.excluir(dado)

        case "4":
            print("Percursos da Árvore")
            print("Pré-Ordem:")
            arvore.pre_ordem(arvore.raiz)
            print("\nEm Ordem:")
            arvore.em_ordem(arvore.raiz)
            print("\nPós-Ordem:")
            arvore.pos_ordem(arvore.raiz)
            print("\nPor Nível:")
            arvore.nivel_ordem()

        case "5":
            print("Saindo do programa...")
            break

        case _:
            print("Opção inválida. Tente novamente.")
