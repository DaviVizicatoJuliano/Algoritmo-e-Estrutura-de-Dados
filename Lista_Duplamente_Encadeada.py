#Atividade 01 - Fila
'''
fila = []
while True:
    print("1. Adicionar Elemento")
    print("2. Remover Elemento")
    print("3. Verificar Tamanho da Lista")
    print("4. Localizar elemento")
    print("5. Verificar Posição do Elemento")
    print("6. Sair")

    op = input("Insira a opção: ")
    
    match op:
        
        case "1":
            element = int(input("Insira o elemento: "))
            fila.append(element)
            print(fila)

        case "2":
            element = int(input("Insira o elemento que deseja excluir: "))
            if element in fila:
                fila.remove(element)  # Remove pelo valor
                print(f"Elemento {element} removido. Fila atual: {fila}")
            else:
                print("Elemento não encontrado na fila!")
            
        case "3":
            print("Quantidade de Elementos: ",len(fila))
        
        case "4":
            element = int(input("Insira o elemento que deseja achar: "))
            if element in fila:
                print(f"Elemento {element} presente na fila")
                
            else:
                print("Elemento não presente na fila!")
            
        case "5":
            element = int(input("Insira o elemento que deseja achar o índice: "))
            if element in fila:
                index = fila.index(element)
                print(f"Elemento {element} encontrado na posição {index}.")
            else:
                print("Elemento não encontrado na fila!")
            
        case "6":
            print("Saindo...")
            break
        
        case _:
            print("Opção Inválida!")
        '''
        
#Atividade 02
'''
from collections import deque as dq

fila = dq([])

while True:
    
    print("1. Adicionar novos clientes a fila")
    print("2. Atender o próximo cliente da fila")
    print("3. Exibir todos os clientes da fila")
    print("4. Sair")
    
    op = input("Insira a opção: ")
    
    match op:
        
        case "1":
            cliente = str(input("Insira o cliente na fila: "))
            fila.append(cliente)
            
        case "2":
            fila.popleft()
            print("Clientes Restantes: ", fila)
            
        case "3":
            print("Clientes na fila: ", fila)
            
        case "4":
            print("Fim do Programa")
            break'''
            
#Exercicio 3 - Gerenciando Histórico de Navegação com Pilha
from collections import deque as dq

historico = dq()

while True:
    print("\n1. Adicionar Página")
    print("2. Remover Página Visitada")
    print("3. Exibir o histórico atual")
    print("4. Limpar Histórico")
    print("0. Sair")
    
    op = input("\nInsira uma opção: ")
    match op:
        
        case "1":
            id_pagina = (input("Insira o ID da Página: "))
            url = input("Insira a URL da página: ")
            data = input("Inserir hora e minuto que acessou a página (HH:MM): ")
            
            pagina = {
                "id": id_pagina,
                "url": url,
                "timestamp": data
            }
            
            historico.appendleft(pagina) 
            print("\nPágina adicionada com sucesso!")

        case "2":
            if historico:
                removido = historico.popleft()
                print("\nPágina removida do histórico:")
                print(removido)
            else:
                print("\nO histórico está vazio.")

        case "3":
            # Exibir o histórico atual
            if historico:
                print("\nHistórico atual:")
                for id,pagina in enumerate(historico):
                    print(f"ID: {pagina['id']} | URL: {pagina['url']} | Timestamp: {pagina['timestamp']}")
            else:
                print("\histórico vazio.")

        case "4":
            # Limpar o histórico
            historico.clear()
            print("\nHistórico limpo com sucesso.")

        case "0":
            # Sair do programa
            print("\nSaind0...")
            break

        case _:
            print("\nOpção inválida")

