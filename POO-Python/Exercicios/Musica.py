# Criar uma classe musica

class Musica:
    nome = ''
    artista = ''
    duracao = float


musicaTrap = Musica()
musicaTrap.nome = 'Life is Good'
musicaTrap.artista = 'Drake'
musicaTrap.duracao = 5.35

print(f"Nome da música: {musicaTrap.nome}\n Artista: {musicaTrap.artista}\n Duração da música: {musicaTrap.duracao} minutos")
print()

musicaRock = Musica()
musicaRock.nome = 'I Wanna Rock'
musicaRock.artista = 'Twisted Sister'
musicaRock.duracao = 4.33
print(f"Nome da música: {musicaRock.nome}\n Artista: {musicaRock.artista}\n Duração da música: {musicaRock.duracao} minutos")
print()
musicaPagode = Musica()
musicaPagode.nome = 'Cheia de manias'
musicaPagode.artista = "Raça Negra"
musicaPagode.duracao = 4.13
print(f"Nome da música: {musicaPagode.nome}\n Artista: {musicaPagode.artista}\n Duração da música: {musicaPagode.duracao} minutos")

