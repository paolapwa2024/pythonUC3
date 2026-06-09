#Crie uma classe Pessoa

class Pessoa:


    def __init__(self, nome, idade):

        self.nome = nome
        self.idade = idade

        print(self.nome)
        print(self.idade)


p = Pessoa("Paola", 35)
