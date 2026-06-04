class Aluno:
    def estudar(self):
        for i in range(5):
            print ("Estou estudando") 

    def vouestudar(resposta):
        if resposta == "sim":
            print("bom estudar!")
        else:
            print("acho que e melhor voce estudar")

aluno = Aluno()
aluno.estudar()
resposta = int ("voce vai estudar hoje")
aluno.vouestudar(resposta)