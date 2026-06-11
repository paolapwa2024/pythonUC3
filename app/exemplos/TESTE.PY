
# SISTEMA BANCÁRIO - Orientado a Objetos


# CLASSE CLIENTE 
class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f"Cliente: {self.nome} | CPF: {self.cpf}"


# CLASSE CONTA (base)
class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular  # um objeto Cliente
        self.saldo = 0.0
        self.historico = []     # lista de transações

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido para saque.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            self.historico.append(f"Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado.")

    def transferir(self, valor, conta_destino):
        if valor <= 0:
            print("Valor inválido para transferência.")
        elif valor > self.saldo:
            print("Saldo insuficiente para transferência.")
        else:
            self.saldo -= valor
            conta_destino.saldo += valor
            self.historico.append(f"Transferência enviada: R$ {valor:.2f} → Conta {conta_destino.numero}")
            conta_destino.historico.append(f"Transferência recebida: R$ {valor:.2f} ← Conta {self.numero}")
            print(f"Transferência de R$ {valor:.2f} realizada.")

    def extrato(self):
        print(f"\n{'='*40}")
        print(f"  EXTRATO - Conta {self.numero}")
        print(f"  Titular: {self.titular.nome}")
        print(f"{'='*40}")
        if not self.historico:
            print("  Nenhuma transação realizada.")
        for item in self.historico:
            print(f"  {item}")
        print(f"\n  Saldo atual: R$ {self.saldo:.2f}")
        print(f"{'='*40}\n")

    def __str__(self):
        return f"Conta {self.numero} | Titular: {self.titular.nome} | Saldo: R$ {self.saldo:.2f}"


# CONTA CORRENTE (herda de Conta
class ContaCorrente(Conta):
    def __init__(self, numero, titular, limite=500.0):
        super().__init__(numero, titular)
        self.limite = limite 

    def sacar(self, valor):
        total_disponivel = self.saldo + self.limite
        if valor <= 0:
            print("Valor inválido para saque.")
        elif valor > total_disponivel:
            print("Saldo + limite insuficientes.")
        else:
            self.saldo -= valor
            self.historico.append(f"Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado.")

    def __str__(self):
        return f"[Corrente] Conta {self.numero} | Titular: {self.titular.nome} | Saldo: R$ {self.saldo:.2f} | Limite: R$ {self.limite:.2f}"


# ---- CONTA POUPANÇA (herda de Conta) ----
class ContaPoupanca(Conta):
    def __str__(self):
        return f"[Poupança] Conta {self.numero} | Titular: {self.titular.nome} | Saldo: R$ {self.saldo:.2f}"


# ============================================
# TESTANDO O SISTEMA
# ============================================

# Criando clientes
cliente1 = Cliente("Ana Silva", "123.456.789-00")
cliente2 = Cliente("Bruno Costa", "987.654.321-00")

# Criando contas
conta1 = ContaCorrente("001", cliente1, limite=300.0)
conta2 = ContaPoupanca("002", cliente2)

print(conta1)
print(conta2)
print()

# Operações
conta1.depositar(1000)
conta2.depositar(500)

conta1.sacar(200)
conta2.sacar(700)  # deve falhar (sem limite)

conta1.transferir(150, conta2)

# Extratos
conta1.extrato()
conta2.extrato()
