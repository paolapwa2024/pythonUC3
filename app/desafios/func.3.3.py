# FUNÇÃO FATORIAL (FOR)


def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)


numero = int(input("Digite um número: "))
print(f"O fatorial de {numero} é {fatorial(numero)}")