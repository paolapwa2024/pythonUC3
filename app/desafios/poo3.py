# Criação da classe
class Contador:

    # Construtor
    def __init__(self):

        self.valor = 0

    # Método para aumentar
    def aumentar(self):

        self.valor += 1

    # Método para diminuir
    def diminuir(self):

        self.valor -= 1


# Criando objeto
contador = Contador()

# Aumentando
contador.aumentar()
contador.aumentar()

# Diminuindo
contador.diminuir()

# Mostrando valor final
print("Valor do contador:", contador.valor)