#Contador simples

class Contador:
    
    def __init__(self):

        self.valor = 0

    def aumentar(self):

        self.valor += 1

    
    def diminuir(self):

        self.valor -= 1

contador = Contador()

contador.aumentar()

contador.diminuir()

print("Valor do contador:", contador.valor)
