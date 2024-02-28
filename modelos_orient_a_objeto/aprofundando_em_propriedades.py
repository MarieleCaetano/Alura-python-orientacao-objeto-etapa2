
class Loja: 
    lojas = []
    def __init__(self, name, category):
        self._name = name.title() # .title serve para deixar todos os nomes de loja com a 1 letra em maius
        #culo
        self._category = category.upper()
        self._ativad = False  #colocando _ antes da categoria faz com q todos os objetos em q eu o usar
        Loja.lojas.append(self) #se tornem privados da classe, sem possibilidade de modificacao por meio
                                #de algum cod fora do def
    def __str__(self):
        return f'{self.name} | {self.category}'
    
    @property 
    def ativad(self):
        return 'verdadeiro' if self._ativad else False

    def alternar_estado(self):
        self._ativad = not self._ativad
        
    @classmethod
    def listar_lojas(cls):
        for loja in cls.lojas:
            print(f'{loja._name} - {loja._category} - {loja._ativad}')
    



loja_bela = Loja('bela', 'Luxo')
loja_bela.alternar_estado()

Loja.listar_lojas()    #esse é tipo um print, estou pedindo para ele listar todos os restaurantes que eu
                        #cadastrei