num1 = float(input("Digite um numero: "))
num2 = float(input("Digite o segundo numero: "))

# Operadores relacionais
print("num1 > num2 :", num1 > num2)
print("num1 >= num2:", num1 >= num2)
print("num1 < num2 :", num1 < num2)
print("num1 <= num2:", num1 <= num2)
print("num1 == num2:", num1 == num2)
print("num1 != num2:", num1 != num2)

# Maior / Menor
if num1 > num2:
    print(f"Maior: {num1}. Menor: {num2}")
elif num1 < num2:
    print(f"Maior: {num2}. Menor: {num1}")
else:
    print("Os dois numeros sao iguais!")

# Maior ou igual
if num1 >= num2:
    print(f"{num1} e maior ou igual a {num2}")
else:
    print(f"{num1} e menor que {num2}")

# Menor ou igual
if num1 <= num2:
    print(f"{num1} e menor ou igual a {num2}")
else:
    print(f"{num1} e maior que {num2}")

# Igualdade
if num1 == num2:
    print(f"{num1} e igual a {num2}")
else:
    print(f"{num1} e diferente de {num2}")

# Diferenca
if num1 != num2:
    print(f"{num1} e diferente de {num2}")
else:
    print(f"{num1} e igual a {num2}")