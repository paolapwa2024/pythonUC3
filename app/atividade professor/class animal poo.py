class Animal:
    def __init__(self, revestimento_externo):
        self.revestimento_externo = revestimento_externo

    def __str__(self):
        return f"tipo de revestimento externo: {self.revestimento_externo}"


class Carnivero(Animal):
    def Comer(self):
        print(" Esta comendo carne")

class Mamifero(Animal):
    def Comer(self):
        print("Está mamando")


Leao = Carnivero("pelos")
print(Leao.Comer())

#Polimorfismo
def come(obj):
    print (obj.comer())

come(Carnivero())
come(Mamifero())