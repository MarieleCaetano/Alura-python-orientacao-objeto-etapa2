class Musica:
    musicas = []
    def __init__(self, nome, artista, duração):
        self.nome = nome
        self.artista = artista
        self.duração = duração
        self._ativo = False    #colocando o underline significa q eu n espero q as pessoas acessem ele
        #direto 
        Musica.musicas.append(self)
    

    def __str__(self):
        return f'{self.nome} - {self.artista} - {self.duração}'
    

    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica.nome} - {musica.artista} - {musica.duração}')

    @property #ESSE COMANDO É, O @ É UM DECORATOR DO PYTHON, QUANDO EU ESCREVO PROPERTY EU TENHO A CAPACIDADE
            #DE PEGAR UM PRODUTO e modificar a forma de como ele será lido, serve tmb para agrupar numero e op matematicas
    def ativo(self):
        return 'verdadeiro' if self.ativo else False
#musica 1
por_do_sol = Musica('Brilho ensolarado', 'Zafon', '12 minutos')

#musica 2
ceu_azul = Musica('Aguas claras', 'antony', '3 minutos')

#musica 3
chuva_de_verao = Musica('gotas dagua', 'clarisse', '4 minutos')

Musica.listar_musicas()
