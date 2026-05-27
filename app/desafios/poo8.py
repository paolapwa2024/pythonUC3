#CLASSE COM CONTADOR DE OBJETOS

class Pessoa:
    total = 0  

    def __init__(self, nome):
        self.nome = nome
        Pessoa.total = Pessoa.total + 1
        print(f"'{self.nome}' criado! Total de pessoas: {Pessoa.total}")

p1 = Pessoa("João")
p2 = Pessoa("Maria")
p3 = Pessoa("Pedro")

print(f"\nTotal de objetos criados: {Pessoa.total}")