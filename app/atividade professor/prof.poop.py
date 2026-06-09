class Teclado:

    def __init__(self, marca, preco,cor):

        self.marca = marca
        self.preco = preco
        self.cor = cor
   
    def __str__(self):
        return f"marca: {self.marca}\n preco: {self.preco}\n cor: {self.cor}"

    def minhafuncao (self):
        return f"marca: {self.marca}\n preco: {self.preco}\n cor: {self.cor}"

TecladoLogtec = Teclado("Logtec","R$ 180.00","Branco")
print(TecladoLogtec)
TecladoOutro = Teclado ("Master", 18.50,"Rosa")
print(TecladoOutro.minhafucao())
