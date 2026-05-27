# === SISTEMA DE LOGIN ===

def login():
    tentativas = 0

    while tentativas < 3:
        senha = input("Digite a senha: ")

        if senha == "paola123":
            print("Acesso liberado!")
            break
        else:
            tentativas = tentativas + 1
            print(f"Senha errada! Tentativas restantes: {3 - tentativas}\n")

    if tentativas == 3:
        print("Acesso bloqueado! Você errou 3 vezes.")


login()