#CONTAR ATÉ N COM WHILE

def contar(n):
    numero = 1
    while numero <= n:
        print(numero)
        numero = numero + 1


n = int(input("Digite até qual número quer contar: "))

contar(n)
