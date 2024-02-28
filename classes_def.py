from modelos_orient_a_objeto.restaurante import Loja

restaurante_praca = Loja('Praça', 'Gourmet')
restaurante_mexicano = Loja('Mexican food', 'Mexicana')
restaurante_japones = Loja('Japa', 'Japonesa')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_japones.receber_avaliacao('Lais', 8)
restaurante_mexicano.receber_avaliacao('Emy', 5)

def main():
    Loja.listar_lojas()
    pass

if __name__ == '__main__':
    main()