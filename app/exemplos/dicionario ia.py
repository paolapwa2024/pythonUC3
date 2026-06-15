# Criando o dicionário do funcionário
funcionario = {
    "nome": "Carlos",
    "idade": 30,
    "cargo": "Júnior"
}

# exercicio 2
print(funcionario["nome"])
print(funcionario["cargo"])

# exercicio 3
funcionario["salário"] = 3500
print(funcionario)

# exercicio 4

funcionario["cargo"] = "Pleno"
print(funcionario)

# exercicio 5

for chave, valor in funcionario.items():
    print(chave, "-", valor)

# exercicio 6

funcionarios = [
    {"nome": "Valdir", "cargo": "gerente"},
    {"nome": "José",  "cargo": "suporte"},
    {"nome": "Maria", "cargo": "analista"}
]

# é a mesma coisa que isso na forma manual:
contador = 1
for f in funcionarios:
    print(contador, f)
    contador = contador + 1
    
# exercicio 7

funcionario.update({
    "cargo": "Sênior",
    "salário": 5000
})
print(funcionario)

# exercicio 8

nome   = input("Digite o nome: ")
idade  = input("Digite a idade: ")
setor  = input("Digite o setor: ")

funcionario_novo = {
    "nome": nome,
    "idade": idade,
    "setor": setor
}

