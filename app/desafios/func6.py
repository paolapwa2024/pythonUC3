# VALIDADOR DE SENHA

def validar_senha():
    while True:
        senha = input("Digite a senha: ")

        if senha == "paola1"3:
            print("Senha correta! Acesso liberado.")
            break
        else:
            print("Senha errada! Tente novamente.\n")

validar_senha()