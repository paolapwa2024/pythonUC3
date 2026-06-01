# TABUADA 

def tabuada(n):
    print(f"Tabuada do {n}:\n")
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)



numero = int(input("Digite um número: "))

tabuada(numero)