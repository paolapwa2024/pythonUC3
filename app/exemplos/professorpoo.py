# Demostartivo de objeto (poo)

class carro:
    def __init__(self,moto,quant_rodas):
        self.moto = moto
        self.quant_rodas = quant_rodas

        def __init__(self):
            pass

class fucionario:
    def __init__(self):
        pass

def andar (self):
    print ("carro esta andando")

class fucionario:
    nome: "Carlos"
    idade: " 0"
    cargo:" "

car1 = carro("v8",4)
car2 = carro("v6",4)
car3 = carro ()
car3.moto = "v12" # tribuindo  valor a propriedade do objeto
print (car3.moto)
car3.andar()# EXECUTANDo A FUNÇAO DO ObJETO

#mostr inrfomação
print("carro 1 tem o moto:",car1.moto)
print("carro 2 tem o moto:",car1.moto)

class cliente:
     def __init__(self,nome,cpf,telefone,email):
         'nome'
         'cpf'
         'telefone'
         'email'
         
         self.nome = ("Maria")
         self.cpf =("014.594.962-13")
         self.telefone = ("(92)96213-3456")
         self.email = ("mari@gmai.com")

cliente = cliente(nome="Maria",cpf= "014.594.962-13",telefone="(92)96213-3456",email="mari@gmai,.com")
print("Nome do cliente:",cliente.nome)
print("CPF do cliente:",cliente.cpf)
print("Telefone do cliente:",cliente.telefone)
print("Email do cliente:",cliente.email)


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
resposta = input ("voce vai estudar hoje")
aluno.vouestudar(resposta)