#Verificação de idade mínima

idade = int(input("informe sua idade: "))
novidade = int(idade)
try:
    if idade >=18 :
        print ("acesso liberado ao sistema")
    else:
        print("Usuario não tem idade para acesso")
        10
except ValueError:
    print("Erro ou informação invalida")



