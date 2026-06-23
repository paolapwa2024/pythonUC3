# CONTAR PARES EM UM INTERVALO 

def contar_pares(inicio, fim):
    total = 0
    numero = inicio

    while numero <= fim:
        if numero % 2 == 0:
            total = total + 1
        numero = numero + 1

    print("Pares entre", inicio, "e", fim, ":", total)


inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))

contar_pares(inicio, fim)
