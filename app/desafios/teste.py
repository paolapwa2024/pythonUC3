class Passaro:
    def voar (self):
        return " Voando alto"
    
class Aviao:
    def voar (self):
        return "Avião em velocidade de cruzeiro"

def decola (obj):
    print(obj.voar())

decola(Passaro())
decola(Aviao())