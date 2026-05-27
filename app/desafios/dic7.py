# Dicionário do exercício anterior
funcionario = {
    "nome"  : "Carlos",
    "idade" : 25,
    "cargo" : "Técnico de TI"
}

funcionario.update({
    "cargo"  : "Sênior",
    "salario": 5000
})

print("=== Ficha do Funcionário ===")
print("Nome:   ", funcionario["nome"])
print("Idade:  ", funcionario["idade"])
print("Cargo:  ", funcionario["cargo"])
print("Salário:", funcionario["salario"])