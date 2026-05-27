# === VERIFICADOR DE FAIXA ETÁRIA ===

def verificar_idade(idade):
    if idade < 12:
        print("Criança")
    elif idade < 18:
        print("Adolescente")
    elif idade < 60:
        print("Adulto")
    else:
        print("Idoso")


idade = int(input("Digite a idade: "))

verificar_idade(idade)