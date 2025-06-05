#Arvore AVL
class Nodo:
    def __init__(self, dado, esquerda=None, direita=None, altura=1):
        self.dado = dado
        self.esquerda = esquerda
        self.direita = direita
        self.altura = altura


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def rotacao_direita(self, nodo_y):

        nodo_x = nodo_y.esquerda
        nodo_t = nodo_x.direita

        nodo_x.direita = nodo_y
        nodo_y.esquerda = nodo_t

        nodo_y.altura = 1 + max(self.altura(nodo_y.esquerda), self.altura(nodo_y.direita))
        nodo_x.altura = 1 + max(self.altura(nodo_x.esquerda), self.altura(nodo_x.direita))

        return nodo_x

    def rotacao_esquerda(self, nodo_x):

        nodo_y = nodo_x.direita
        nodo_t = nodo_y.esquerda

        nodo_y.esquerda = nodo_x
        nodo_x.direita = nodo_t

        nodo_y.altura = 1 + max(self.altura(nodo_y.esquerda), self.altura(nodo_y.direita))
        nodo_x.altura = 1 + max(self.altura(nodo_x.esquerda), self.altura(nodo_x.direita))

        return nodo_y

    def inserir_chave(self, valor):
        self.raiz = self.inserir(self.raiz, valor)

    def inserir(self, raiz, chave):

        if not raiz:
            return Nodo(chave)

        if chave > raiz.dado:
            raiz.direita = self.inserir(raiz.direita, chave)
        elif chave < raiz.dado:
            raiz.esquerda = self.inserir(raiz.esquerda, chave)
        else:
            return raiz #Evitar repetição de número

        raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita))

        balanceamento = self.balanceamento(raiz)

        # Rotação Direita-Direita
        if balanceamento > 1 and chave < raiz.esquerda.dado:
            return self.rotacao_direita(raiz)

        # Rotação Esquerda-Esquerda
        if balanceamento < -1 and chave > raiz.direita.dado:
            return self.rotacao_esquerda(raiz)

        # Rotação Direita-Esquerda
        if balanceamento > 1 and chave > raiz.esquerda.dado:
            raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
            return self.rotacao_direita(raiz)

        # Rotação Esquerda-Direita
        if balanceamento < -1 and chave < raiz.direita.dado:
            raiz.direita = self.rotacao_direita(raiz.direita)
            return self.rotacao_esquerda(raiz)

        return raiz

    def altura(self, nodo):
        if not nodo:
            return 0
        else:
            return nodo.altura

    def balanceamento(self, nodo):
        if not nodo:
            return 0
        else:
            return self.altura(nodo.esquerda) - self.altura(nodo.direita)

    def em_ordem(self):
        self._em_ordem_recursivamente(self.raiz)

    def _em_ordem_recursivamente(self, raiz):

        if raiz:
            self._em_ordem_recursivamente(raiz.esquerda)
            print(raiz.dado, end=" ")
            self._em_ordem_recursivamente(raiz.direita),

    def pre_ordem(self):
        self._pre_ordem_recursivamente(self.raiz)

    def _pre_ordem_recursivamente(self, raiz):
        if raiz:
            print(raiz.dado, end=" ")
            self._pre_ordem_recursivamente(raiz.esquerda)
            self._pre_ordem_recursivamente(raiz.direita),

    def pos_ordem(self):
        self._pos_ordem_recursivamente(self.raiz)

    def _pos_ordem_recursivamente(self, raiz):

        if raiz:
            self._pos_ordem_recursivamente(raiz.esquerda)
            self._pos_ordem_recursivamente(raiz.direita),
            print(raiz.dado, end=" ")

    def em_nivel(self):
        self._em_nivel_recursivamente(self.raiz)

    def _em_nivel_recursivamente(self):
        if self.raiz is None:
            return None
        
        fila = [self.raiz]
        while fila:
            atual = fila.pop(0)
            print(atual.dado, end=" ")
            if atual.esquerda:
                fila.append(atual.esquerda)
            if atual.direita:
                fila.append(atual.direita)

    def excluir(self, raiz, chave):
        if not raiz:
            return raiz

        if chave < raiz.dado:
            raiz.esquerda = self.excluir(raiz.esquerda, chave)
        elif chave > raiz.dado:
            raiz.direita = self.excluir(raiz.direita, chave)
        else:
            # Caso 1: Nó folha
            if not raiz.esquerda and not raiz.direita:
                return None

            # Caso 2: Um único filho
            if not raiz.esquerda:
                return raiz.direita
            elif not raiz.direita:
                return raiz.esquerda

            # Caso 3: Dois filhos
            temp = self.min_valor_nodo(raiz.direita)
            raiz.dado = temp.dado
            raiz.direita = self.excluir(raiz.direita, temp.dado)

        # Atualiza altura
        raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita))

        # Verifica balanceamento
        balanceamento = self.balanceamento(raiz)

        # Rotação Direita-Direita
        if balanceamento > 1 and self.balanceamento(raiz.esquerda) >= 0:
            return self.rotacao_direita(raiz)

        # Rotação Esquerda-Esquerda
        if balanceamento < -1 and self.balanceamento(raiz.direita) <= 0:
            return self.rotacao_esquerda(raiz)

        # Rotação Direita-Esquerda
        if balanceamento > 1 and self.balanceamento(raiz.esquerda) < 0:
            raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
            return self.rotacao_direita(raiz)

        # Rotação Esquerda-Direita
        if balanceamento < -1 and self.balanceamento(raiz.direita) > 0:
            raiz.direita = self.rotacao_direita(raiz.direita)
            return self.rotacao_esquerda(raiz)

        return raiz

    def buscar(self,raiz,nodo):
        
        if not raiz:
            return None
        
        if raiz.dado == nodo:
            return nodo
        
        if nodo < raiz.dado:
            return self.buscar(raiz.esquerda,nodo)
        else:
            return self.buscar(raiz.direita,nodo)

AVL = ArvoreBinaria()

while True:
    print("\n=== MENU ÁRVORE AVL ===")
    print("1. Inserir Elemento")
    print("2. Excluir Elemento")
    print("3. Buscar Elemento")
    print("4. Exibir em Ordem")
    print("5. Exibir em Pré-Ordem")
    print("6. Exibir em Pós-Ordem")
    print("7. Exibir em Nível")
    print("0. Sair")
    
    op = input("Insira sua escolha: ")
    
    match op:
        
        case "1":  # Inserção
            valor = int(input("Insira o elemento: "))
            AVL.inserir_chave(valor)
            print(f"Elemento {valor} inserido com sucesso!")

        case "2":  # Exclusão
            valor = int(input("Insira o elemento a ser excluído: "))
            AVL.raiz = AVL.excluir(AVL.raiz, valor)
            print(f"Elemento {valor} excluído, se existia.")

        case "3":  # Busca
            valor = int(input("Digite o elemento a ser buscado: "))
            encontrado = AVL.buscar(AVL.raiz, valor)
            if encontrado:
                print(f"Elemento {valor} encontrado!")
            else:
                print(f"Elemento {valor} não encontrado!")

        case "4":  # Em Ordem
            print("Exibição em Ordem:")
            AVL.em_ordem()

        case "5":  # Pré-Ordem
            print("Exibição em Pré-Ordem:")
            AVL.pre_ordem()

        case "6":  # Pós-Ordem
            print("Exibição em Pós-Ordem:")
            AVL.pos_ordem()

        case "7":
            print("Exibição em Nível:")
            AVL.em_nivel()

        case "0":  # Sair
            print("Saindo... Até mais!")
            break

        case _:  # Opção inválida
            print("Opção inválida! Tente novamente.")