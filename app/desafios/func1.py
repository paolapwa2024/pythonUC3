# === PAR OU ÍMPAR COM FUNÇÃO ===



def verificar_par(num):
    if num % 2 == 0:
        print(num, "é PAR.")
    else:
        print(num, "é ÍMPAR.")



numero = int(input("Digite um número: "))

verificar_par(numero)