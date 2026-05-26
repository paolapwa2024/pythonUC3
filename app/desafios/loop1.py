# Pede um número positivo
numero = int(input("Digite um número positivo: "))

# Repete enquanto o número for inválido
while numero < 0:
    print("Número inválido!")

    numero = int(input("Digite novamente: "))

# Mensagem final
    print("Número válido:", numero)