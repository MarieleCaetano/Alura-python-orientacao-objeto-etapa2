class musica:
    nome = ''
    artista = ''
    duracao = int

#musica 1
por_do_sol = musica()
por_do_sol.nome = 'Brilho ensolarado'
por_do_sol.artista = 'Zafon'
por_do_sol.duracao = 12

#musica 2
ceu_azul = musica()
ceu_azul.nome = 'Aguas claras'
ceu_azul.artista = 'Antony'
ceu_azul.duracao = 3

#musica 3
chuva_de_verao = musica()
chuva_de_verao.nome = 'Gotas dagua'
chuva_de_verao.artista = 'clarise'
chuva_de_verao.duracao = 4


print(vars(por_do_sol))
print(vars(ceu_azul))
print(vars(chuva_de_verao))


#modo de resolução da alura
class Musica:
    nome = ''
    artista = ''
    duracao = int


musica1 = Musica()
musica1.nome = 'Bohemian Rhapsody'
musica1.artista = 'Queen'
musica1.duracao = 355

musica2 = Musica()
musica2.nome = 'Imagine'
musica2.artista = 'John Lennon'
musica2.duracao = 183

musica3 = Musica()
musica3.nome = 'Shape of You'
musica3.artista = 'Ed Sheeran'
musica3.duracao = 234

