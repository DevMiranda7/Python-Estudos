class Musica:
    musicas = []
    def __init__(self, nome,artista,duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def exibirMusicas():
        for musica in Musica.musicas:
            print(f"Nome da música: {musica.nome}\n Artista: {musica.artista}\n Duração: {musica.duracao}")

    

musica = Musica("No Friends in The Industry","Drake",3.24)
musica1 = Musica("Wild Thoughts","DJ Khaled ft. Rihanna, Bryson Tiller",3.35)
musica2 = Musica("EVERY CHANCE I GET","DJ Khaled - ft. Lil Baby, Lil Durk",3.56)
Musica.exibirMusicas()