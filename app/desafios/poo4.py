# CLASSE PRODUTO 

class Produto:
    def __init__(self, nome, preco):
        self.nome  = nome
        self.preco = preco

    def aplicar_desconto(self, desconto):
        self.preco = self.preco - (self.preco * desconto / 100)
        print(f"Desconto de {desconto}% aplicado!")
        print(f"Novo preço de {self.nome}: R$ {self.preco:.2f}")


produto1 = Produto("Tênis", 200)


produto1.aplicar_desconto(10)