# SOMAR POSITIVOS PULANDO NEGATIVOS

numeros = [-1, 2, -3, 4]
total = 0

for numero in numeros:
    if numero < 0:
        continue
    total = total + numero

print("Soma dos positivos:", total)