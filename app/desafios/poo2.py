# Classe Aluno com método estudar

class Aluno:

    def __init__(self, nome):

        self.nome = nome

    def estudar(self):

        print(self.nome, "está estudando.")


aluno1 = Aluno("Paola")

aluno1.estudar()




