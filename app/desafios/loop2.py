# Variável para guardar a soma
total = 0

# Número inicial
numero = 1

# Repete enquanto o número for diferente de 0
while numero != 0:

    numero = int(input("Digite um número (0 para parar): "))

    total = total + numero

# Mostra o resultado final
print("Total da soma:", total)