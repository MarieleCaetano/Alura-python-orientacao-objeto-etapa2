
class restaurante: #classes é todos os detalhes que quero em algo, ex um carro, quais detalhes ele
#precisa ter? quantidade de rodas, cor, assentos etc.
    nome = ''
    categoria = ''     #exemplo simples do que é uma classe, ele retorna um endereço 'ox108d00810'
    ativo = False        # apos eu digitar no terminal: python modelos_orient_a_objeto/restaurante.py

restaurante_vitta = restaurante()
restaurante_vitta.nome= 'Bistro'
restaurante_vitta.categoria = 'Gourmet'

print(dir(restaurante_vitta)) #DIR é uma funcao que mostra mais atributos sobre a classe ou alguma
                                #outra coisa que eu quiser ver os atributos, tipo um help, ideal para 
                                #quando existe uma classe que a gente nao conhece.
print(vars(restaurante_vitta))# VARS é uma funcao que mostra os atributos definidos por mim na funcao, 
                                #mostrando 'nome' 'vitta' 'categoria' 'gourmet', mas n mostra o 'ativo'
print(restaurante_vitta.ativo) # ATIVO esta armazenado porem no vars ele nao me retorna o valor ao menos
                                # que eu peça com .ativo,me retornando o valor false, definido na linha 5
print(f'Nome do restaurante: {restaurante_vitta.nome})')
if restaurante_vitta.ativo:
    print('O restaurante esta ativo')
else:
    print('O restaurante esta inativo')

categoria = restaurante_vitta.categoria

restaurante_pizza = restaurante()
restaurante_pizza.nome = 'Pizza place'
restaurante_pizza.categoria = 'Fast food'
restaurante_pizza.ativo = True

if restaurante_pizza.categoria == 'Fast food':
    print(f'{restaurante_pizza.nome} é um restaurante {restaurante_pizza.categoria}')
else:
    print(f'{restaurante_pizza.nome} não é da categoria fast food')


#--------------
#aula 1 - contrutor e instanciando objetos par 2 do curso
#AULA 2 - METODOS ESPECIAIS PART 2 DO CURSO
    
class Restaurante:
    def __init__(self, Nome, Categ): 
                           #Def init serve para definir, por ex todas as informacoes que eu passar
        self.Nome = Nome   #do restaurante brasil, vão ser do restaurante brasil, o mesmo vale para qualquer
        self.Categ = Categ #outro restaurante que for fornecido os dados nome, categ e ativo
        self.ativ = False  # ali entre () temos o nome, categoria, que serve para dizer que dessa instancia
                    #eu espero o nome e categoria. SELF ou THIS antes do nome e categoria entre () serve pra
                           #dizer que se trata daquele objeto que eu estiver referenciando naquele momento
                           # se for o restaurante brasil entao os dados nome e cat seram da instancia 
                           # do restaurante brasil
                           #agora se eu criar um restaurante sem dizer o nome e categ ele vai dar um erro
                           #pedindo pelo nome e categoria do restaurante
    def __str__(self):     #lembrando q self serve para dizer q se rest brasil chamar ou qualquer outro
        return f'{self.Nome} | {self.Categ}'   #ele é pra servir
restaurante_brasil = Restaurante('Brasil', 'fastfood') #entre () estou definindo o nome e a categ do meu
                                                       # restaurante
#existe um metodo para dizer ao meu programa que quero que ele me retorne um valor em texto quando 
#eu printar o restaurante brasil, que é o __str__
print(restaurante_brasil) 

#AULA 3 - CRIANDO MEUS METODOS ESPECIAIS
from modelos_orient_a_objeto.avaliação import Avaliacao
class Loja: #Nome de classe sempre com a primeira letra em maiusculo
    lojas = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.ativad = False
        self._avaliacao = []
        Loja.lojas.append(self)

    def __str__(self):
        return f'{self.name} | {self.category}'
    

    def listar_lojas():
        for loja in Loja.lojas:
            print(f'{loja.name.ljust(25)} | {loja.category.ljust(25)} | {loja.ativad.ljust(25)} | {loja.media_avaliacoes.ljust(25)}')

    @property 
    def ativo(self):
        return 'verdadeiro' if self._ativad else False

    def alternar_estado(self):
        self._ativo = not self._ativo
    
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao) 
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao) #sum é a soma, pedindo pra somar
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)#round serve para arredondar o result da
        #media, por ex se sair 3,454 vai ser so 3,4 pois coloquei o 1 apos a virgula no final
        return media
    
loja_bela = Loja('Bela', 'Luxo')

Loja.listar_lojas()    #esse é tipo um print, estou pedindo para ele listar todos os restaurantes que eu
                        #cadastrei