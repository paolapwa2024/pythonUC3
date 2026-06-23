#ÍMPARES PULANDO MÚLTIPLOS DE 7 

def impares_sem_multiplos_de_7(inicio, fim):
    for numero in range(inicio, fim + 1):

        if numero % 2 == 0:
            continue

        if numero % 7 == 0:
            continue  
        print(numero)

       

inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))

impares_sem_multiplos_de_7(inicio, fim)
