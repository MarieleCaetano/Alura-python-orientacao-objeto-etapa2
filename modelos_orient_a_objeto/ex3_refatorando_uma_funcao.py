class Pessoa:
    def __init__(self, nome='', profissao='', idade=0):
        self.nome = nome
        self.profissao = profissao
        self.idade = idade

    def __str__(self):
        if self.profissao:
            return f'{self.nome} trabalha de {self.profissao} e tem {self.idade} idade'
        else:
            return f'{self.nome} tem {self.idade} de idade'

    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome} trabalho como {self.profissao}'
        else:
            return f'Olá sou {self.nome}'

    def aniversario(self):
        self.idade += 1

#criando 3 instancias da classe pessoa
pessoa1 = Pessoa(nome='Julia', profissao= 'artista', idade = 24)
pessoa2 = Pessoa(nome = 'Antonio', profissao='Carpinteiro', idade= 47)
pessoa3 = Pessoa(nome='Rachel', idade= 30)

#imprimindo informacoes iniciais
print('Informações iniciais')
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

#utilizando o metodo instancia de aniversario

pessoa1.aniversario()
pessoa3.aniversario()

#imprimindo informaçòes após aniversário

print('Informações após aniversário')
print(pessoa1)
print(pessoa3)
print()

#utilizando o metodo classe
print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)
