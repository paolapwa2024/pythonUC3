#CLASSE COM CONTADOR DE OBJETOS

class Objetos:
    total = 0  

    def __init__(self, nome):
        self.nome = nome
        Objetos.total = Objetos.total + 1
        print(f"'{self.nome}' criada!  Total de objetos:  {Objetos.total}")

o1 = Objetos("Bola")
o2 = Objetos("Arvore")
o3 = Objetos("Boneca")

print(f"\nTotal de objetos criados: {Objetos.total}")