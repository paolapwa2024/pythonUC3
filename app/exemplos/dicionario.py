pesssoa = {
    "nome": "Ana",
    "cpf": "014.523.245-12",
    "telefone" : 91989598408

}

print(pesssoa)
print (pesssoa["cpf"])
pesssoa["nome"] = "luisa"
print(pesssoa["nome"])

for chave, valor in pesssoa.items():
    print(f"Seu {chave} é {valor}")