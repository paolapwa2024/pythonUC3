#Requisitos do Sistema 

class Cliente:
    def __init__(self, nome, CPF):
        self.nome = nome
        self.CPF = CPF

    def __str__(self):
        return f"Cliente: {self.nome} | CPF: {self.CPF}"


class Conta:
    def __init__(self, numero_da_conta, titular, saldo=0):
        self.numero_da_conta = numero_da_conta
        self.titular = titular
        self.saldo = saldo
        self.extrato = []


class Operacoes(Conta):
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado.")
        else:
            print("Valor inválido para saque.")

    def transferir(self, valor, conta_destino):
        if 0 < valor <= self.saldo:
             self.sacar(valor)
             conta_destino.depositar(valor)
             print(f"Transferência de R$ {valor:.2f} realizada.")
             print(f"De: {self.titular.nome} / Para: {conta_destino.titular.nome}")
        else:
             print("Valor inválido para transferência.")

    def consultar(self):
             extrato = "\n  ".join(self.extrato)
             print(f"\n Conta: {self.titular.nome} ")
             print(f"Saldo: R$ {self.saldo:.2f}\nExtrato:\n  {extrato}\n")


class Conta_Corrente(Operacoes):
    def __init__(self, numero, titular, limite, saldo=0):
        Operacoes.__init__(self, numero, titular, saldo)
        self.limite = limite

    def sacar(self, valor):  # sobrescreve o sacar — usa o limite
        if 0 < valor <= self.saldo + self.limite:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado.")
        else:
            print("Valor inválido para saque.")


class Conta_Poupança(Operacoes):  # sem limite extra
    def __init__(self, numero, titular, saldo=0):
        Operacoes.__init__(self, numero, titular, saldo)



Cliente1 = Cliente("Paola", "014.594.962-12")
print(Cliente1)
conta1 = Conta_Corrente("001", Cliente1, limite=1000)
conta1.depositar(500)
conta1.sacar(100)
conta1.consultar()


Cliente2 = Cliente("Willian", "014.594.962-14")
print(Cliente2)
conta2 = Conta_Corrente("002", Cliente2, limite=1000, saldo=7000.00)
conta2.depositar(700)
conta2.sacar(1500)
conta2.consultar()


print("Transferência")
conta1.depositar(1000)
conta1.transferir(200, conta2)
conta1.consultar()
conta2.consultar()