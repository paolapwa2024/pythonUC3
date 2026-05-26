# Pede o usuário
usuario = input("Digite o usuário: ")

# Pede a senha
senha = input("Digite a senha: ")

# Verifica usuário e senha
if usuario == "admin" and senha == "1234":
    print("Bem-vindo!")
else:
    print("Usuário ou senha incorretos.")