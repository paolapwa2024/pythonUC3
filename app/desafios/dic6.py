# Criando a lista com 3 funcionários
funcionarios = [
    {"id": 1, "nome": "Valdir", "cargo": "Gerente"},
    {"id": 2, "nome": "José",   "cargo": "Suporte"},
    {"id": 3, "nome": "Maria",  "cargo": "Analista"}
]

for f in funcionarios:
    print("id:", f["id"], "  - nome:", f["nome"], "  - cargo:", f["cargo"])