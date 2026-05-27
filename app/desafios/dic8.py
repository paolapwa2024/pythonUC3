# Pedindo os dados para o usuário
nome   = input("Digite o nome: ")
idade  = input("Digite a idade: ")
setor  = input("Digite o setor: ")

funcionario = {
    "nome"  : nome,
    "idade" : idade,
    "setor" : setor
}

print("=== Ficha do Funcionário ===")
print("Nome:  ", funcionario["nome"])
print("Idade: ", funcionario["idade"])
print("Setor: ", funcionario["setor"])