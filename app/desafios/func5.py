# CALCULADORA SIMPLE

def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y


print("Digite dois números inteiros...")
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
op = input("Qual operação (+ ou -): ")

if op == "+":
    print("Resultado:", somar(n1, n2))
elif op == "-":
    print("Resultado:", subtrair(n1, n2))
else:
    print("Operação inválida!")