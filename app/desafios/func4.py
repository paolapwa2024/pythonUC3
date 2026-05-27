# === SOMA ATÉ DIGITAR 0 ===

def somar_valores():
    total = 0

    while True:
        numero = int(input("Digite um número (0 para parar): "))

        if numero == 0:
            break

        total = total + numero
        print(f"Somando... total até agora: {total}")

    print(f"\nVocê parou! Total final: {total}")

somar_valores()