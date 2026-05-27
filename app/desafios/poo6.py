# CLASSE VEICULO E SUBCLASSES

class Veiculo:
    def __init__(self, marca, velocidade):
        self.marca      = marca
        self.velocidade = velocidade

    def mover(self):
        print(f"{self.marca} está se movendo a {self.velocidade} km/h!")


class Carro(Veiculo):
    def ligar_ar(self):
        print(f"{self.marca} ligou o ar condicionado!")


class Moto(Veiculo):
    def fazer_wheeling(self):
        print(f"{self.marca} fez um wheeling!")


carro = Carro("Toyota", 120)
moto  = Moto("Honda", 90)

carro.mover()
carro.ligar_ar()

moto.mover()
moto.fazer_wheeling()