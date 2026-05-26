# Criação da classe
class Aluno:

    # Método construtor
    def __init__(self, nome):

        self.nome = nome

    # Método estudar
    def estudar(self):

        print(self.nome, "está estudando.")


# Criando objeto
aluno1 = Aluno("Paola")

# Chamando o método
aluno1.estudar()