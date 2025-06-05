class Musica:
    def __init__(self,dado,proximo = None,anterior = None):
        self.dado = dado
        self.proximo = proximo
        self.anterior = anterior
        
class Playlist:
    def __init__(self):
        self.cabeca = None
        self.musica_atual = None
        
    def adicionar_musica(self,titulo):
        nova_musica = Musica(titulo)
        if not self.cabeca:
            self.cabeca = nova_musica 
        else:    
            atual = self.cabeca 
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = nova_musica
            nova_musica.anterior = atual
        print("Musica Inserida!")
        
    def exibir_playlist(self):
        if not self.cabeca:
            print("A lista está vazia")
            return
        
        atual = self.cabeca
        playlist = []
        while atual:
            playlist.append(atual.dado)
            atual = atual.proximo
            
        print("Musica na Playlist: ", "<-->".join(map(str,playlist)))
        
    def alterar_titulo(self,titulo_atual,novo_titulo):
        if not self.cabeca:
            print("Playlist Vazia")
            return
        atual = self.cabeca
        while atual:
            if atual.dado == titulo_atual:
                atual.dado = novo_titulo
                print(f"Musica {titulo_atual} alterado para {novo_titulo}")
                return
            atual = atual.proximo
        print(f"Música {titulo_atual} não encontrado na playlist")
        
    def excluir_musica(self,titulo):
        if not self.cabeca:
            print("Playlist esta vazia")
            return
        
        atual = self.cabeca
        while atual:
            if atual.dado == titulo:
                if atual.anterior:
                    atual.anterior.proximo = atual.proximo
                else:
                    self.cabeca = atual.proximo
                if atual.proximo:
                    atual.proximo.anterior = atual.anterior
                print(f"Musica {titulo} removido com sucesso da playlist\n")
                return
            atual = atual.proximo
        print(f"Musica {titulo} não encontrado na playlist")
        
    def tocar_proxima(self):
        if not self.cabeca:
            print("Playlist Vazia!")
            return
        
        if self.musica_atual is None:
            self.musica_atual = self.cabeca
        
        print("Musica Atual: ", self.musica_atual.dado)
        
        if self.musica_atual.proximo:
            self.musica_atual = self.musica_atual.proximo
        else:
            print("Você chegou ao final da playlist.")
            self.musica_atual = None
            
    def tocar_anterior(self):
        if not self.cabeca:
            print("Playlist Vazia!")
            return
        
        if self.musica_atual.anterior:
            self.musica_atual = self.musica_atual.anterior
            print("Musica Atual: ",self.musica_atual.dado)
        else:
            print("Você chegou no inicio da fila!")
            print("Musica Atual: ",self.musica_atual.dado)
        
tocar = Playlist()

'''tocar.adicionar_musica("November Rain")
tocar.adicionar_musica("Fifty Cent")
tocar.adicionar_musica("Back in Black")
tocar.alterar_titulo("Fifty Cent","Guns N Roses")
tocar.tocar_proxima()
tocar.tocar_proxima()
tocar.tocar_anterior()S
tocar.exibir_playlist()
'''
while True:
    print("1.Adicionar uma Nova Musica")
    print("2.Remover uma musica")
    print("3.Alterar o titulo de uma Musica")
    print("4.Tocar a Proxima Musica")
    print("5.Tocar a Musica Anterior")
    print("6.Exibir todas as Musicas da playlist")
    print("0.Sair")
    op = str(input("Insira a opção: "))
    
    match op:
        
        case "1":
            new = str(input("Insira a nova musica: "))
            tocar.adicionar_musica(new)
            
        case "2":
            music = str(input("Insira a musica que deseja apagar: "))
            tocar.excluir_musica(music)
            
        case "3":
            music_atual = str(input("Insira a musica que deseja alterar: "))
            new_name = str(input("Insira o novo nome: "))
            tocar.alterar_titulo(music_atual,new_name)
            
        case "4":
            tocar.tocar_proxima()
            
        case "5":
            tocar.tocar_anterior()
            
        case "6":
            tocar.exibir_playlist()
        
        case "0":
            print("Fim do Programa")
            break
        
        case default:
            print("Opção invalida!")