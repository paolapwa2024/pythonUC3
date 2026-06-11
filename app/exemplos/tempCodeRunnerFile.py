#Requisitos do Sistema 

class Cliente:
    def __init__(self, nome , CPF):
        self.nome = nome
        self.CPF = CPF

    def __str__(self):
        return f"Cliente: {self.nome} | CPF: {self.CPF}"
    
Cliente1 = Cliente("Paola","014.594.962-12")
print(Cliente1)

class Conta:
    def __init__(self,numero_da_conta, titular, saldo=0):
        self.numero_da_conta = numero_da_conta
        self.titular = titular
        self.saldo = saldo
        self.extrato = []
   

class Operacoes( Conta ):
    #def __init__(self,depositar, sacar, transferencia):
       # self.depositar = depositar
      #  self.sacar = sacar
       # self.transferencia = transferencia
    

    def depositar(self,valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f" Depósito de R$ {valor:.2f} realizado.")
        else:
            print("Valor inválido para depósito.")

    def sacar (self,valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            print(f" Saque de R$ {valor:.2f} realizado.")
        else:
            print("Valor inválido para saque.")

    def transferir(self, valor, conta_destino):
        if 0 < valor <= self.saldo:
            self.sacar(valor)
            conta_destino.depositar(valor)
            print(f"Transferência de R$ {valor:.2f} realizada.")
        else:
            print("Valor inválido para transferência.")
    
    def consultar(self,valor):
        if valor


 
class Conta_Corrente(Operacoes):
    def __init__(self, numero, titular, limite):
        Operacoes.__init__(numero, titular)
        self.limite = limite

class Conta_Poupança(Operacoes):
    def __init__(self, numero, titular):
        Operacoes.__init__(numero, titular)
