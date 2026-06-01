# === SOMA ATÉ ZERO ===

total = 0

while True:
    numero = int(input("Digite um número (0 para parar): "))

    if numero == 0:
        break

    total = total + numero

print("Soma total:", total)