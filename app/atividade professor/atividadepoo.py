#atividade da função de objeto( POO)

class Alimento:
    def __init__(self, semente, casca):
        self.semente = semente  
        self.casca = casca

    def Fruta(self):
        for i in range(1):
            print("semente grande")

    def polpa(self):
        print("fina")

    def madura(self):
        print("A fruta está madura!")



alimento = Alimento("semente grande", "casca fina")
alimento.Fruta()
alimento.polpa()

fruta3 = Alimento("semente", "casca")
fruta3.semente = "redonda"   
print(fruta3.semente)
fruta3.madura()