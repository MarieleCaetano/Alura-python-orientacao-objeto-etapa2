class Musica:
    musicas = []
    def __init__(self, nome, artista, duração):
        self.nome = nome
        self.artista = artista
        self.duração = duração
        Musica.musicas.append(self)
    

    def __str__(self):
        return f'{self.nome} - {self.artista} - {self.duração}'
    

    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica.nome} - {musica.artista} - {musica.duração}')


#musica 1
por_do_sol = Musica('Brilho ensolarado', 'Zafon', '12 minutos')

#musica 2
ceu_azul = Musica('Aguas claras', 'antony', '3 minutos')

#musica 3
chuva_de_verao = Musica('gotas dagua', 'clarisse', '4 minutos')

Musica.listar_musicas()
