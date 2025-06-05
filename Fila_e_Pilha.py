class NodoLista:
    def __init__(self,dado = 0, proximo_nodo = 0):
        self.dado = dado
        self.proximo = proximo_nodo
        
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)
    
class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        
    def __repr__(self):
        return "[" + str(self.cabeca) + "]"
    
    def insere_no_inicio(self,novo_dado):
        novo_nodo = NodoLista(novo_dado)
        novo_nodo.proximo = self.cabeca
        self.cabeca = novo_nodo
        print("Numero Inserido com sucesso! \n")
    
    def Busca(self, valor):
        corrente = self.cabeca
        while corrente and corrente.dado != valor:
            corrente = corrente.proximo
        if corrente:
            print("Valor Encontrado: ", corrente)
        else:
            print("Valor Não Encontrado!")
        
    
    def Remove(self,valor):
        assert self.cabeca
        
        if self.cabeca.dado == valor:
            self.cabeca = self.cabeca.proximo
        else:
            anterior = None
            corrente = self.cabeca
        while corrente and corrente.dado != valor:
            anterior = corrente
            corrente = corrente.proximo
            
        if corrente:
            anterior.proximo = corrente.proximo
        else:
            anterior.proximo = None
            
    def Alterar(self,valor):
        assert self.cabeca
        
        if self.cabeca.dado == valor:
            self.cabeca = self.cabeca.proximo
        else:
            anterior = None
            corrente = self.cabeca
        while corrente and corrente.dado != valor:
            anterior = corrente
            corrente = corrente.proximo
            
        if corrente:
            new = float(input("Insira o novo valor: "))
            corrente.dado = new
        else:
            anterior.proximo = None
            
    def Exibir(self):
        print("Elementos Inseridos: ")
        corrente = self.cabeca
        while corrente:
            print(corrente.dado)
            corrente = corrente.proximo
        print()
    
lista = ListaEncadeada()   

while True:
    
    print("1.Inserir Elemento")
    print("2.Remover Elemento")
    print("3.Buscar Elemento")
    print("4.Alterar Elemento")
    print("5.Exibir Elementos")
    print("6.Sair")
    
    op = int(input("Insira sua opção: "))
    
    match op:
        
        case 1:
            num = str(input("Insira o elemento: "))
            lista.insere_no_inicio(num)
            
        case 2:
            num = str(input("Insira o elemento que deseja remover: "))
            lista.Remove(num)
            
        case 3:
            num = str(input("Insira o elemento que deseja buscar: "))
            lista.Busca(num)
            
        case 4:
            num = str(input("Insira o elemento que deseja alterar: "))
            lista.Alterar(num)
            
        case 5:
            lista.Exibir()
            
        case 6:
            print("Fim do Programa")
            break
        
        case default:
            print("Opção Inválida!")
