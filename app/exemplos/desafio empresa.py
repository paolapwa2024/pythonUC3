#Requisitos do Sistema 

class Cliente:
    def __init__(self, Nome , CPF):
        self.Nome = Nome
        self.CPF = CPF
class Conta:
    def __init__(self,Numero_da_conta, Titular, Saldo):
        self.Numero_da_conta = Numero_da_conta
        self.Titular = Titular
        self.Saldoaldo = Saldo
 

class Operacoes:
    def __init__(self,Depositar, Sacar, Transferencia, Colsultar_Saldo):
        self.Depositar = Depositar
        self.Sacar = Sacar
        self.Transferencia = Transferencia


Operações 

Depositar  

Sacar  

Transferir  

Consultar saldo  

Conta Corrente 

Possui limite extra para saque. 

Conta Poupança 

Não possui limite extra. 