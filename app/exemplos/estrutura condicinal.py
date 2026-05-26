# Consultar maior de idade 
idade = 20 

if idade>=18:
    print(" maior de idade")


# Confirma ou validar senha
if senha == 131400:
    print(" Acesso Liberado ")

else: 
    print(" Acesso Negado ")


 # Avaliar notas
nota = 8

if nota >= 8:
    print('Excelente')

elif nota >= 7:
    print(" Aprovado")

elif nota >= 5:
    print("Recuperação")

else:
    print("Reprovado")


# while

contador = 0
while contador<5:
    print("contador")
    contador += 1
    contador = contador +1


# Range infinito 0
# Range e 0 a 4
for numero in range(0):
     if numero == 5:
        print(numero)


# Range com break
for numero in range(0):
        if numero == 5:
            break
        print(numero)

# Pular numero
for numero in range(10):
        if numero == 5:
            continue
        print(numero)

    