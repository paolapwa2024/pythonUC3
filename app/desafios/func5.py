#FUN

def ADICAO (x, y):
    w = x + y
    return w
def SUBTRACAO(x, y):
    return x - y

print("Digite dois valores inetiros...")
n1 = int(input("x: "))
n2 = int(input("y: "))
op = input("Qual operacao (+ ou -)?")

if op == "+":
    z = ADICAO (n1, n2)
    print("Resultado da soma:", z)
elif op == "-":
    z = SUBTRACAO (n1, n2)
    print("Resultado da subtracao:", z)
else:
    print("Saiu!")