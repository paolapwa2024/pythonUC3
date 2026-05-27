#Leitura repetida até entrada válida

numero = int(input("Digite um número positivo: "))


while numero < 0:
    print("Número inválido!")

    numero = int(input("Digite novamente: "))


    print("Número válido:", numero)